import numpy as np
import laspy
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from scipy.spatial import Delaunay
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

# Here we take only the first 1000 points for simplicity.
# You could take more points depending on your computational power.
x = point_cloud[0:1000, 0]
y = point_cloud[0:1000, 1]
z = point_cloud[0:1000, 2]

# Create 3D scatter plot
sp = gl.GLScatterPlotItem(pos=point_cloud, color=pg.glColor((0, 0, 255)), size=0.1, pxMode=True)
w.addItem(sp)

# Create surface using Delaunay triangulation
tri = Delaunay(np.column_stack((x, y)))
vertices = np.array([point_cloud[i] for i in tri.simplices])

# Create mesh item and add to view
m1 = gl.GLMeshItem(vertexes=vertices, drawEdges=True, smooth=True, shader='balloon')
w.addItem(m1)

# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()

