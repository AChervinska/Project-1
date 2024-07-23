import cv2
from matplotlib import pyplot as plt

# Opening image
img = cv2.imread("testPhoto.jpg")

# Ensure the image is loaded correctly
if img is None:
    raise FileNotFoundError("The image file was not found or could not be opened.")

# OpenCV opens images as BRG but we want it as RGB and we also need a grayscale version
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Creates the environment of the picture and shows it
plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
