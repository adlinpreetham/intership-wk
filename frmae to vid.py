import cv2
import os

# Path to the folder containing frames
frames_folder = "C:/Users/Lenovo/Downloads/adlin"
# Output video file path (including the filename)
output_video_path = "C:/Users/Lenovo/Downloads/preetgam/output.mp4"

# Get the list of frames in the folder
frame_files = [f for f in os.listdir(frames_folder) if f.endswith('.jpg')]

# Sort the frames based on their filenames
frame_files.sort()

# Read the first frame to get dimensions
first_frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
height, width, _ = first_frame.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can choose other codecs like 'XVID' or 'MJPG'
video_writer = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

# Write frames to the video
for frame_file in frame_files:
    frame_path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(frame_path)
    
    if frame is not None:
        video_writer.write(frame)
    else:
        print(f"Failed to read frame: {frame_file}")

# Release the VideoWriter object
video_writer.release()

print(f"Video saved to {output_video_path}")
