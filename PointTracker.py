import numpy as np
import matplotlib.pyplot as plt
import cv2
import plotly.express as px
path = "/home/saklani/Projects/PointTracker/video/box.mp4"

cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(count)

frames =np.zeros((count, height, width,3), dtype=int)
print(frames.shape)
for i in range(count):
    ret, frame = cap.read()
   # print(i)
    if ret == True:
        frames[i] = frame
indices_of_dot = []
for frame in frames:
    r = frame[:,:,2]
    g = frame[:,:,1]
    b = frame[:,:,0]
    mask = (r>100) & (g<35) & (b < 30)
    row, col = np.where(mask)
#print(row, col)
    indices_of_dot.append((row, col))
 #   print(indices_of_dot)
    ''' if(i == 2):
        break
    i=2

#print(indices_of_dot)
#%%
#print(frames[0,734 ,517,:])
#%%
#arr[34,17]
#%%
#frames[0, 999,732]
#%%

'''
