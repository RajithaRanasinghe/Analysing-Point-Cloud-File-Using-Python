import numpy as np
import laspy
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore
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
x = point_cloud[0:100, 0]
y = point_cloud[0:100, 1]
z = point_cloud[0:100, 2]

g = gl.GLGridItem()
w.addItem(g)


# Create 3D scatter plot
sp = gl.GLScatterPlotItem(pos=point_cloud, pxMode=True)
w.addItem(sp)

# Start Qt event loop and keep it running
sys.exit(app.exec_())
