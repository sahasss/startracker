import zipfile
import os

# Define paths
zip_path = r"C:\Users\MUTHUS\star_tracker_project\star_tracker_project\final-star-tracker-input.zip"  # Update this with the correct zip file name
extract_path = "star_images"  # Folder to extract images

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print(f"Dataset extracted to: {extract_path}")
