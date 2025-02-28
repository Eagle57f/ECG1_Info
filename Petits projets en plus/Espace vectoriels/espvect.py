import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib


base = np.array([[1, 1, -2],
                 [1, -2, 1],
                 [2, 3, -2]])
n=2
vect=[]

for i in range(-n, n+1):
    for j in range(-n, n+1):
        for k in range(-n, n+1):
            vect.append(((i,j,k), np.linalg.solve(base.T, np.array([i, j, k]))))


fig = plt.figure()
ax = plt.axes(projection='3d')
for (i,j,k), (x,y,z) in vect:
    ax.quiver(i, j, k, x, y, z, color='r')
plt.title(base)
plt.show()

# def rotate(angle):
#     ax.view_init(elev=angle)

# rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
# rot_animation.save(fr'{pathlib.Path(__file__).parent.absolute()}\rotation.gif', dpi=120, writer='imagemagick')