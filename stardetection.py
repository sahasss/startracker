import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Define dataset path
image_folder = r"C:\Users\MUTHUS\star_tracker_project\star_tracker_project\star_images"  # Update this path if needed

# Get all PNG images
image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]

# Process each image
for image_file in image_files:  
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Find contours (stars)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw detected stars
    output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green boxes around stars

    # Display results
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title(f"Original Image: {image_file}")

    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title("Detected Stars")

    plt.show()
