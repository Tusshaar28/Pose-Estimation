import cv2
import numpy as np
import matplotlib.pyplot as plt
from angles import calcangle
import mediapipe as mp
from model import detectimg
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.3, model_complexity=2)

def classifyPose(landmarks, output_image, display=False):
    '''
    This function classifies human poses depending upon the angles of various body joints.
    Args:
        landmarks: A list of detected landmarks of the person whose pose needs to be classified.
        output_image: An image of the person with the detected pose landmarks drawn.
        display: A boolean value that if set to true the function displays the resultant image with the pose label
        written on it and returns nothing.
    Returns:
        output_image: The image with the detected pose landmarks drawn and pose label written.
        label: The classified pose label of the person in the output_image.
    '''

    # Initialize the label of the pose. It is not known at this stage.
    label = 'Unknown Pose'

    # Specify the color (Red) with which the label will be written on the image.
    color = (0, 0, 255)

    # Calculate the required angles.
    # ----------------------------------------------------------------------------------------------------------------

    # Get the angle between the left shoulder, elbow and wrist points.
    lelbow = calcangle(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                       landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                       landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

    # Get the angle between the right shoulder, elbow and wrist points.
    relbow = calcangle(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

    # Get the angle between the left elbow, shoulder and hip points.
    lshol = calcangle(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
                      landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                      landmarks[mp_pose.PoseLandmark.LEFT_HIP.value])

    # Get the angle between the right hip, shoulder and elbow points.
    rshol = calcangle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                      landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])

    # Get the angle between the left hip, knee and ankle points.
    lknee = calcangle(landmarks[mp_pose.PoseLandmark.LEFT_HIP.value],
                      landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value],
                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value])

    # Get the angle between the right hip, knee and ankle points
    rknee = calcangle(landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value],
                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value],
                      landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value])
    print(f"Left Elbow Angle: {lelbow:.2f}")
    print(f"Right Elbow Angle: {relbow:.2f}")
    print(f"Left Shoulder Angle: {lshol:.2f}")
    print(f"Right Shoulder Angle: {rshol:.2f}")
    print(f"Left Knee Angle: {lknee:.2f}")
    print(f"Right Knee Angle: {rknee:.2f}")


    # ----------------------------------------------------------------------------------------------------------------

    # Poses.

    if 160 <= lelbow <= 240 and 50 <= relbow <= 200 and 170 <= lknee <= 190 and 100 <= rknee <= 190:
        label = 'Standing'

    elif 100 <= lelbow <= 160 and 30 <= relbow <= 160 and  250 <= lknee <= 290 and 250 <= rknee <= 290:
        label = 'Sitting'

    elif ((lelbow > 250 or lelbow < 80) and (relbow > 200 or relbow < 80)  and (270 <= lshol <= 360 or 0 <= lshol <= 60) and(0 <= rshol <= 40 or 270 <= rshol <= 360) and (lknee <= 200 or lknee>290) and (rknee <= 200 or rknee > 290)):
             label = 'Sleeping'
    elif (120 <= lelbow <= 210 and 160 <= relbow <= 230 and
          (10 <= lshol <= 40 or 330 <= lshol <= 360) and (10 <= rshol <= 20 or 330 <= rshol <= 360) and
          160 <= lknee <= 195 and 170 <= rknee <= 195):
        label = 'Walking'


    if label != 'Unknown Pose':
        color = (0, 255, 0)

    cv2.putText(output_image, label, (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)


    if display:
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')
        plt.show()
    else:
        return output_image, label

img = cv2.imread('vidoes/wk2.jpeg')
out, lm = detectimg(img,pose, display=False)
if lm:
    classifyPose(lm,out, display=True)