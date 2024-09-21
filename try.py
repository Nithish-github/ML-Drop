import torch
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# Image source
img = "https://ultralytics.com/images/zidane.jpg"  # URL image or local image file

# Perform inference
results = model(img)

# Print the results (e.g., classes, confidence, bounding boxes)
results.print()

r_img = results.render() # returns a list with the images as np.array
print(r_img)
img_with_boxes = r_img[0] # image with boxes as np.array

cv2.imwrite("result.png",img_with_boxes)
# Show the image with bounding boxes using .show()
# results.show()  # Displays the image in a pop-up window (for local use)

# # Alternatively, save the image with bounding boxes
# results.save(save_dir='runs/detect/')  # Saves image with boxes in the directory 'runs/detect/'

# Display the saved image using matplotlib (for environments without .show() pop-up functionality)
# saved_image_path = 'runs/detect/exp/zidane.jpg'  # Adjust path as needed

# # Read and display the saved image with bounding boxes using OpenCV and matplotlib
# img_with_boxes = cv2.imread(saved_image_path)
# img_with_boxes = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

# plt.imshow(img_with_boxes)
# plt.axis('off')  # Hide axes
# plt.show()
