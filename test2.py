import numpy as np
import cv2
# from matplotlib import pyplot as plt

img1 = cv2.imread('fotos/box1.jpg',cv2.IMREAD_GRAYSCALE)          # queryImage
img2 = cv2.imread('fotos/cenario100.jpg') # trainImage

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)

cv2.imshow('img',img3)
k = cv2.waitKey(0) & 0xFF    