import cv2
import numpy as np

print(cv2.__version__)

image = cv2.imread("image/test.jpg", cv2.IMREAD_UNCHANGED)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()