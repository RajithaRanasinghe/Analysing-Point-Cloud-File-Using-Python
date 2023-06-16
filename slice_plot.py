import numpy as np
import laspy
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import sys
import matplotlib.pyplot as plt

# Load the LAS file
in_file = laspy.read('Unnamed.las')

# Extract X, Y, and Z coordinates
x = in_file.x
y = in_file.y
z = in_file.z

# Create a NumPy array from the coordinates
point_cloud = np.column_stack((x, y, z))

# Here we take only the first 1000 points for simplicity.
PCD_POINTS = 100000

dx = point_cloud[0:PCD_POINTS, 0]
dy = point_cloud[0:PCD_POINTS, 1]
dz = point_cloud[0:PCD_POINTS, 2]

dx = dx + abs(np.min(dx))
dy = dy + abs(np.min(dy))
dz = dz + abs(np.min(dz))


#Inclicnation correction
for i, zi in enumerate (dz):
    #print(f'{dz[i]} {(0.132 * dy[i])}  {dy[i]}')
    dz[i] = dz[i] - (0.135 * dx[i])
    #print(f'{dz[i]}')


new_point_cloud = np.column_stack((dx , dy, dz))

# Define slice thickness
slice_thickness = 0.1

# Get median of X and Y
median_x = np.median(dx)
median_y = np.median(dy)

# Get points within the middle slice in X direction
slice_mask_x = np.logical_and(dx > median_x - slice_thickness, dx < median_x + slice_thickness)

# Get points within the middle slice in Y direction
slice_mask_y = np.logical_and(dy > median_y - slice_thickness, dy < median_y + slice_thickness)

# Get points within the middle slice in both X and Y directions
slice_mask_xy = np.logical_and(slice_mask_x, slice_mask_y)

# Extract slices
slice_x = new_point_cloud[slice_mask_x]
slice_y = new_point_cloud[slice_mask_y]
slice_xy = new_point_cloud[slice_mask_xy]

# Plot the slices
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(slice_x[:, 1], slice_x[:, 2], s=1)
plt.title('Middle slice in X direction')

plt.subplot(1, 3, 2)
plt.scatter(slice_y[:, 0], slice_y[:, 2], s=1)
plt.title('Middle slice in Y direction')

plt.subplot(1, 3, 3)
plt.scatter(slice_xy[:, 0], slice_xy[:, 2], s=1)
plt.title('Middle slice in both X and Y directions')

plt.tight_layout()
plt.show()
