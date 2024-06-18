from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os

# Function to draw landmarks on image
def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks
    annotated_image = np.copy(rgb_image)

    for idx in range(len(pose_landmarks_list)):
        pose_landmarks = pose_landmarks_list[idx]

        pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
        pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
        ])
        solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style())
    return annotated_image

# Set up MediaPipe PoseLandmarker
base_options = python.BaseOptions(model_asset_path='/opt/venv/pose_landmarker.task')
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    output_segmentation_masks=True)
detector = vision.PoseLandmarker.create_from_options(options)

# Open the video file
video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Create a directory to save the frames
output_dir = 'output_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each frame
frame_count = 0
fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate the timestamp
    timestamp = frame_count / fps

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create MediaPipe image object
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Detect pose landmarks
    detection_result = detector.detect(image)

    # Annotate the frame with landmarks
    annotated_frame = draw_landmarks_on_image(rgb_frame, detection_result)

    # Convert RGB frame back to BGR for OpenCV
    annotated_frame_bgr = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)

    # Save the annotated frame as an image file with the timestamp
    output_filename = os.path.join(output_dir, f'frame_{frame_count:04d}_timestamp_{timestamp:.2f}.jpg')
    cv2.imwrite(output_filename, annotated_frame_bgr)

    frame_count += 1

# Release everything when done
cap.release()

print(f"Annotated frames saved successfully in {output_dir}.")
