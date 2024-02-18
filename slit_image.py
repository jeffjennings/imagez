import numpy as np
import matplotlib.pyplot as plt
import cv2

vid_file = 'roses.mp4'
vid_file = 'control2.mp4'

vid = cv2.VideoCapture(vid_file)
nframe = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(f"Video has {nframe} frames at {fps} FPS")

# plot first frame
_, frame0 = vid.read()
# flip BGR to RGB
frame0 = frame0[:,:,::-1]
plt.figure()
plt.imshow(frame0)
plt.title('Frame 0')
plt.show()

