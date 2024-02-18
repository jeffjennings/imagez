import numpy as np
import matplotlib.pyplot as plt
import cv2

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

# user selects row or column of each frame used to make slit image
rc = input("Slice on 'col' or 'row'?\n")
idx = int(input("Slice index?\n"))
target_fps = int(input("Sampling FPS?\n"))
if target_fps > fps:
    print("Your selected sampling FPS exceeds video FPS. Defaulting to video FPS.")
    target_fps = fps
decimation_factor = round(fps / target_fps)

# frames = []
slits = []
counter = 0
for ii in range(nframe - 1):
    if ii % decimation_factor == 0:
        print(f"\rframe {ii}", end='', flush=True)
        _, frame = vid.read()
        # flip BGR to RGB
        frame = frame[:,:,::-1]
        # build slit image
        if rc == 'row':
            slits.append(frame[idx,:,:])
        else:
            slits.append(frame[:,idx,:])

        # store frame halfway through video
        tol = 0.01
        if 1 - tol <= ii / (nframe / 2) <= 1 + tol:
            framemid = frame
        
        counter += 1

# flip x, y slit image dimensions
if rc == 'col':
    slits = np.transpose(slits, (1, 0, 2))

fig, ax = plt.subplots(2, 2)
ax = ax.ravel()
fig.set_size_inches(12,12)
ax[0].imshow(frame0)
ax[0].set_title('First frame')
ax[1].imshow(framemid)
ax[1].set_title('Median frame')
ax[2].imshow(frame)
ax[2].set_title('Last frame')
ax[3].imshow(slits, origin='upper')
ax[3].set_title(f'Slit image ({rc} {idx} over {counter} frames)')
plt.tight_layout()
plt.show(block=False)
