import numpy as np
import laspy
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore
from scipy.interpolate import griddata
import sys

## Create a GL View widget to display data
app = pg.mkQApp("GLSurfacePlot Example")
w = gl.GLViewWidget()
w.show()
w.setWindowTitle("example")
w.setCameraPosition(distance=50)

# Load the LAS file
in_file = laspy.read('Unnamed.las')

# Extract X, Y, and Z coordinates
x = in_file.x
y = in_file.y
z = in_file.z

# Create a NumPy array from the coordinates
point_cloud = np.column_stack((x, y, z))

# Here we take only the first 1000 points for simplicity.
# You could take more points depending on your computational power.
x = point_cloud[0:1000, 0]
y = point_cloud[0:1000, 1]
z = point_cloud[0:1000, 2]

g = gl.GLGridItem()
w.addItem(g)

# Create grid coordinates
grid_x, grid_y = np.mgrid[min(x):max(x):100j, min(y):max(y):100j]

# Interpolate z values to create grid
grid_z = griddata((x, y), z, (grid_x, grid_y), method='cubic')

# Normalize z values to range 0-1
grid_z = (grid_z - np.nanmin(grid_z)) / (np.nanmax(grid_z) - np.nanmin(grid_z))

# Create 3D surface plot
sp = gl.GLSurfacePlotItem(z=grid_z, shader='heightColor')
sp.scale((max(x)-min(x))/100, (max(y)-min(y))/100, 1)  # scale to match original x-y scale
sp.translate(min(x), min(y), 0)  # translate to match original x-y positions
w.addItem(sp)

# Start Qt event loop and keep it running
sys.exit(app.exec_())
