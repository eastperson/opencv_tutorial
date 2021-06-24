import cv2

image = cv2.imread("image/test.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Moon", image)

# 높이, 너비, 채널 값
height,width,channel = image.shape
# 400 600 3
print(height,width,channel)

cv2.waitKey()
cv2.destroyAllWindows()