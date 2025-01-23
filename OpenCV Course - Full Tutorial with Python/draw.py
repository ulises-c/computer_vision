import cv2 as cv
import numpy as np


blank = np.zeros(
    (500, 500, 3), dtype="uint8"
)  # creates blank image, 500x500, 3 color channels
# cv.imshow("Blank", blank)

# img = cv.imread("Photos/cat.jpg")
# cv.imshow("image", img)

# 1. Paint image a certain color
# blank[200:300, 300:400] = 255, 0, 0  # B,G,R
# cv.imshow("color", blank)

# 2. Draw a rectangle
cv.rectangle(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (0, 255, 0),
    thickness=cv.FILLED,
)
# cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(
    blank,
    (blank.shape[1] // 2, blank.shape[0] // 2),
    40,
    (0, 0, 255),
    thickness=cv.FILLED,
)
# cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(
    blank,
    (0, 0),
    (blank.shape[1] // 2, blank.shape[0] // 2),
    (255, 0, 0),
    thickness=1,
)
# cv.imshow("Line", blank)

# 5. Write text
cv.putText(
    blank,
    "Hello",
    (225, 225),
    cv.FONT_HERSHEY_TRIPLEX,
    1.0,
    (255, 255, 255),
    2,
)
cv.imshow("Text", blank)

cv.waitKey(0)
