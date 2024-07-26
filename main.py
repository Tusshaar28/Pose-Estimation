import math
import cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

# Initializing mediapipe pose class.
mp_pose = mp.solutions.pose

# Setting up the Pose function.
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

# Initializing mediapipe drawing class, useful for annotation.
mp_drawing = mp.solutions.drawing_utils

sample_img = cv2.imread('vidoes/img.png')

# Specify a size of the figure.
plt.figure(figsize=[5, 5])

# Display the sample image, also convert BGR to RGB for display.
plt.title("Sample Image");
plt.axis('off');
plt.imshow(sample_img[:, :, ::-1]);
# plt.show()

# Perform pose detection after converting the image into RGB format.
results = pose.process(cv2.cvtColor(sample_img, cv2.COLOR_BGR2RGB))

# Check if any landmarks are found.
'''if results.pose_landmarks:
    for i in range(5):
        print(f'{mp_pose.PoseLandmark(i).name}:\n{results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value]}')

image_height, image_width, _ = sample_img.shape
print(sample_img.shape)
# Check if any landmarks are found.
if results.pose_landmarks:
    # Iterate two times as we only want to display first two landmark.
    for i in range(5):  #Convert in image scale
        print(f'{mp_pose.PoseLandmark(i).name}:')
        print(f'x: {results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].x * image_width}')
        print(f'y: {results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].y * image_height}')
        print(f'z: {results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].z * image_width}')
        print(f'visibility: {results.pose_landmarks.landmark[mp_pose.PoseLandmark(i).value].visibility}\n')'''

# Create a copy of the sample image to draw landmarks on.
img_copy = sample_img.copy()

# Check if any landmarks are found.
if results.pose_landmarks:
    # Draw Pose landmarks on the sample image.
    mp_drawing.draw_landmarks(image=img_copy, landmark_list=results.pose_landmarks,
                              connections=mp_pose.POSE_CONNECTIONS)
    mp_drawing.plot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
    # Specify a size of the figure.
    fig = plt.figure(figsize=[10, 10])

    # Display the output image with the landmarks drawn, also convert BGR to RGB for display.
    plt.title("Output");
    plt.axis('off');
    plt.imshow(img_copy[:, :, ::-1]);
    plt.show()
