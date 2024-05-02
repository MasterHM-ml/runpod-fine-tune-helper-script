import os
import shutil
import numpy as np

total_images = 1278
test_indices = np.random.randint(0,total_images-1,50)

# os.makedirs("datasets/train/images")
# os.makedirs("datasets/train/labels")

os.makedirs("datasets/test/images")
os.makedirs("datasets/test/labels")

os.makedirs("datasets/val")

import cv2
vid = cv2.VideoCapture("input_videos/1_short_video.mp4")
s, f = vid.read()
index=1
while s:
    cv2.imwrite(f"datasets/train/images/1_short_video_{index}.png", f)
    s, f = vid.read()
    index+=1
vid.release()

for index in test_indices:
    shutil.move(f"datasets/train/labels/1_short_video_{index}.txt", "datasets/test/labels")
    shutil.move(f"datasets/train/images/1_short_video_{index}.png", "datasets/test/images") 

shutil.copy("datasets/test/images", "datasets/val")
shutil.copy("datasets/test/labels", "datasets/val")
