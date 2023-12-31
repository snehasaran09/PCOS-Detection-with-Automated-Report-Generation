# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 22:36:02 2023

@author: Sneha Saravanan
"""

from PIL import Image
import os

def rotate_images(folder_path, angle):
    # Create a new folder to store the rotated images
    output_folder = f"{folder_path}_rotated"
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate through each file
    for filename in file_list:
        # Check if the file is an image
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Open the image file
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Rotate the image
            rotated_image = image.rotate(angle)

            # Save the rotated image
            new_filename = f"rotated_{angle}_{filename}"
            new_path = os.path.join(output_folder, new_filename)
            rotated_image.save(new_path)
            print(f"Rotated image: {new_filename}")

    print("Rotation complete.")

# Specify the folder path containing the images and the rotation angle in degrees
folder_path = "C:\\Users\\Sneha Saravanan\\Desktop\\College Work\\B.Tech-Year3\\6th Sem\\Capstone\\PCOS\\Datasets\\Combined Dataset\\Proper"
rotation_angle = 45

# Call the function to rotate the images
rotate_images(folder_path, rotation_angle)
