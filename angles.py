import math
import cv2
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt


def calcangle(lm1, lm2, lm3):
    '''
    This function calculates angle between three different lms.
    Args:
        lm1: The first lm containing the x,y and z coordinates.
        lm2: The second lm containing the x,y and z coordinates.
        lm3: The third lm containing the x,y and z coordinates.
    Returns:
        angle: The calculated angle between the three lms.

    '''

    # Get the required lms coordinates.
    x1, y1, z1 = lm1
    x2, y2, z2 = lm2
    x3, y3, z3 = lm3

    # Calculate the angle between the three points
    angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))

    # Check if the angle is less than zero.
    if angle<0:

        # Add 360 to the found angle.
        angle += 360

    # Return the calculated angle.
    return angle


ans = calcangle((500,23,18),(327,328,10),(13,234,100))
print(ans)