# Reference: https://docs.opencv.org/master/d8/d19/tutorial_stitcher.html

import cv2


# Test 1. Sequential inputs.
# inputs = [
#     cv2.imread("inputs/1.jpeg"),
#     cv2.imread("inputs/2.jpeg"),
#     cv2.imread("inputs/3.jpeg"),
#     cv2.imread("inputs/4.jpeg"),
#     cv2.imread("inputs/5.jpeg")
# ]

# Test 2. Random inputs.
inputs = [
    cv2.imread("inputs/2.jpeg"),
    cv2.imread("inputs/4.jpeg"),
    cv2.imread("inputs/1.jpeg"),
    cv2.imread("inputs/5.jpeg"),
    cv2.imread("inputs/3.jpeg")
]

stitcher = cv2.createStitcher(False)
panorama = stitcher.stitch(inputs)[1]    # The first value in the tuple is an integer.

cv2.imshow("Panorama", panorama)
cv2.waitKey(0)
