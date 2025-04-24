import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Set the dataset directory
image_folder = r"C:\Users\MUTHUS\star_tracker_project\star_tracker_project\star_images"  # Update this with your dataset path
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])

# Set up the SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds (you might need to experiment with these values)
params.minThreshold = 10      # Lower threshold for blob detection.
params.maxThreshold = 250

   # Upper threshold.

# Filter by Area.
params.filterByArea = True
params.minArea = 5            # Minimum area of blob (experiment, e.g., 5-20)
params.maxArea = 150          # Maximum area to consider (e.g., to remove large artifacts)

# Filter by Circularity.
params.filterByCircularity = True
params.minCircularity = 0.1   # Stars are roughly circular; adjust as needed.

# Filter by Convexity.
params.filterByConvexity = True
params.minConvexity = 0.5     # Adjust if needed; stars tend to be convex.

# Filter by Inertia (elongation).
params.filterByInertia = True
params.minInertiaRatio = 0.2  # Lower value accepts more elliptical shapes.

# Create a detector with the above parameters
detector = cv2.SimpleBlobDetector_create(params)

# Process a few images to test
for image_file in image_files[:3]:
    image_path = os.path.join(image_folder, image_file)
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Detect blobs (potential stars)
    keypoints = detector.detect(image)
    
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the circle size corresponds to the blob size.
    image_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    # Display the results
    plt.figure(figsize=(10, 5))
    plt.imshow(image_with_keypoints, cmap="gray")
    plt.title(f"Detected Stars in {image_file} - {len(keypoints)} stars")
    plt.axis("off")
    plt.show()
    
    input("Press Enter to continue to the next image...")

