import os
import cv2
import numpy as np

# Specify the file path
file_path = 'image.png'

# Check if the file exists
if os.path.exists(file_path):
    print("File exists at the specified path.")
else:
    print("File does not exist at the specified path.")

# Load the image
image = cv2.imread(file_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours to find circle contours
circle_contours = []
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    if len(approx) >= 6:  # Adjust this threshold as needed
        circle_contours.append(contour)

# Draw contours for visualization
cv2.drawContours(image, circle_contours, -1, (0, 255, 0), 2)

# Find the tip of the clock hand
longest_tip = None
longest_length = 0
a = 0

# Find the extreme points of the contour
leftmost_point = tuple(contour[contour[:, :, 0].argmin()][0])
rightmost_point = tuple(contour[contour[:, :, 0].argmax()][0])
base_point = tuple(contour[contour[:, :, 1].argmax()][0])
tip_point = tuple(contour[contour[:, :, 1].argmin()][0])

# Calculate the length of the tip
tip_length = np.linalg.norm(np.array(tip_point) - np.array(base_point))
tip_length1 = np.linalg.norm(np.array(tip_point) - np.array(base_point))
tip_length2 = np.linalg.norm(np.array(leftmost_point) - np.array(base_point))
tip_length3 = np.linalg.norm(np.array(rightmost_point) - np.array(base_point))
if(tip_length1>tip_length2 and tip_length1>tip_length3) : tip_length = np.linalg.norm(np.array(tip_point) - np.array(base_point))
elif (tip_length2>tip_length1 and tip_length2>tip_length3) :  tip_length = np.linalg.norm(np.array(leftmost_point) - np.array(base_point))
elif (tip_length3>tip_length1 and tip_length3>tip_length2) :  tip_length = np.linalg.norm(np.array(rightmost_point) - np.array(base_point))

# Check if this tip is longer than the previous longest one
if tip_length > longest_length:
    longest_length = tip_length
    longest_tip = tip_point

if(tip_length1>tip_length2 and tip_length1>tip_length3) : longest_tip = tip_point
elif (tip_length2>tip_length1 and tip_length2>tip_length3) :  longest_tip = leftmost_point
elif (tip_length3>tip_length1 and tip_length3>tip_length2) :  longest_tip = rightmost_point

# Draw circles at the base and tip points for visualization
cv2.circle(image, base_point, 5, (0, 0, 255), -1)
cv2.circle(image, tip_point, 5, (0, 0, 255), -1)

# Draw circles at the leftmost and rightmost points for visualization
cv2.circle(image, leftmost_point, 5, (255, 0, 0), -1)
cv2.circle(image, rightmost_point, 5, (255, 0, 0), -1)

# Calculate the vector from the base to the longest tip
vector = np.array([longest_tip[0] - base_point[0], longest_tip[1] - base_point[1]])

# Calculate the angle of the vector
angle = np.arctan2(vector[1], vector[0]) * 180 / np.pi

# Adjust the angle to be between 0 and 180 degrees
if angle < 0:
    angle += 180

print("Clock hand angle:", angle)

# Draw the line representing the clock hand
cv2.line(image, base_point, longest_tip, (0, 255, 0), 2)

# Display the result
cv2.imshow('Clock Hand', image)
cv2.waitKey(0)
cv2.destroyAllWindows()