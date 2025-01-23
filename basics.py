import cv2 as cv
from read import rescale_frame

img = cv.imread("Photos/cat.jpg")
img = rescale_frame(img)  # Image is large so rescaling
cv.imshow("Cat", img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Blur, can be useful to remove noise
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# Edge Cascade, finds edges present in image
canny = cv.Canny(img, 125, 175)
# cv.imshow("Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow("Eroded", eroded)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# Cropping, array slicing
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
