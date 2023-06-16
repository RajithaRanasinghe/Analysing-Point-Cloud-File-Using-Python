import numpy as np
import laspy
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore

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

x = point_cloud[0:1000, 0]
y = point_cloud[0:1000, 1]
z = point_cloud[0:1000, 2]

print('x {} y {} z {}'.format(len(x), len(y), len(z)))

