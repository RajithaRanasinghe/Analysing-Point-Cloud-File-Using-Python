import numpy as np
import laspy
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore
import sys
import matplotlib.cm as cm
import matplotlib.colors as mcolors

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
PCD_POINTS = 10000

dx = point_cloud[0:PCD_POINTS, 0]
dy = point_cloud[0:PCD_POINTS, 1]
dz = point_cloud[0:PCD_POINTS, 2]

minx = np.min(dx)
maxx = np.max(dx)

miny = np.min(dy)
maxy = np.max(dy)

minz = np.min(dz)
maxz = np.max(dz)

dx = dx + abs(minx)
dy = dy + abs(miny)
dz = dz + abs(minz)

minz_adjusted = np.min(dz)
maxz_adjusted = np.max(dz)

new_point_cloud = np.column_stack((dx , dy, dz))

g = gl.GLGridItem()
w.addItem(g)

# Normalizing z values for color mapping
dz_normalized = (dz - minz_adjusted) / (maxz_adjusted - minz_adjusted)

# Create a color map
cmap = cm.get_cmap('jet')  # Choose any color map
rgba_img = cmap(dz_normalized)
#rgba_img = cmap(dz)

# Convert colors to 0-255 range for PyQtGraph
colors = (255 * rgba_img).astype(np.ubyte)

# Create 3D scatter plot
sp = gl.GLScatterPlotItem(pos=new_point_cloud, color=colors, pxMode=True)
w.addItem(sp)

# Start Qt event loop and keep it running
sys.exit(app.exec_())
