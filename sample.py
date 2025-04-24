import cv2
import numpy as np

# Create a blank image
image = np.zeros((300, 300), dtype=np.uint8)

# Draw a white circle (simulating a star)
cv2.circle(image, (150, 150), 10, (255, 255, 255), -1)

# Show the image
cv2.imshow("Test Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

