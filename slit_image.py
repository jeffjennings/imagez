import numpy as np
import matplotlib.pyplot as plt
import cv2

vid_file = 'roses.mp4'
vid_file = 'control2.mp4'

vid = cv2.VideoCapture(vid_file)
nframe = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(f"Video has {nframe} frames at {fps} FPS")

