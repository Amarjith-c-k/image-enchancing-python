import cv2
import numpy as np
from scipy.ndimage import maximum_filter, minimum_filter

img = cv2.imread('rose.png', 0)
# Create our sharpening kernel, the sum of all values must equal to one for uniformity
kernel_sharpening = np.array([[-1,-1,-1],
                              [-1, 9,-1],
                              [-1,-1,-1]])

# Applying the sharpening kernel to the grayscale image & displaying it.
print("\n\n--- Effects on S&P Noise Image with Probability 0.5 ---\n\n")

# Applying filter on image with salt & pepper noise
sharpened_img = cv2.filter2D(img, -1, kernel_sharpening)
cv2.imshow("AF",sharpened_img)
cv2.waitKey(0)

def midpoint(img):
    maxf = maximum_filter(img, (3, 3))
    minf = minimum_filter(img, (3, 3))
    midpoint = (maxf + minf) / 2
    cv2.imshow("midpoint",midpoint)
    

print("\n\n---Effects on S&P Noise Image with Probability 0.5---\n\n")
midpoint(img)
cv2.waitKey(0)