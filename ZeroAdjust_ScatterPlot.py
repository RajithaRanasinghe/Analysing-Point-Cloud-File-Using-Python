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

print(f'before x ({minx},{maxx}) y ({miny},{maxy}) z ({minz},{maxz})')


dx = dx + abs(minx)
dy = dy + abs(miny)
dz = dz + abs(minz)

minx = np.min(dx)
maxx = np.max(dx)

miny = np.min(dy)
maxy = np.max(dy)

minz = np.min(dz)
maxz = np.max(dz)

print(f'after x ({minx},{maxx}) y ({miny},{maxy}) z ({minz},{maxz})')


#Inclicnation correction
for i, zi in enumerate (dz):
    #print(f'{dz[i]} {(0.132 * dy[i])}  {dy[i]}')
    dz[i] = dz[i] - (0.135 * dy[i])
    #print(f'{dz[i]}')


new_point_cloud = np.column_stack((dx , dy, dz))

g = gl.GLGridItem()
w.addItem(g)


# Create 3D scatter plot
sp = gl.GLScatterPlotItem(pos=new_point_cloud, pxMode=True)
w.addItem(sp)

# Start Qt event loop and keep it running
sys.exit(app.exec_())
