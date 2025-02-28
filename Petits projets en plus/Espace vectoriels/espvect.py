import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pathlib


base = np.array([[1, -1, -1],
                 [1, 1, 1],
                 [-1, -1, 1]])
n=2

vect=[]
for i in range(-n, n+1):
    for j in range(-n, n+1):
        for k in range(-n, n+1):
            vect.append(((i,j,k), np.linalg.solve(base.T, np.array([i, j, k]))))


fig = plt.figure()
ax = plt.axes(projection='3d')

vect_list=[]
for (i,j,k), (x,y,z) in vect:
    ax.quiver(i, j, k, x, y, z, color='r')
    vect_list.append((i, j, k, x, y, z))
plt.title(base)



x_min, x_max = np.inf, -np.inf
y_min, y_max = np.inf, -np.inf
z_min, z_max = np.inf, -np.inf


for i in range(len(vect_list)):
    
    x_min = min(x_min, vect_list[i][0], vect_list[i][0] + vect_list[i][3])
    x_max = max(x_max, vect_list[i][0], vect_list[i][0] + vect_list[i][3])
    
    y_min = min(y_min, vect_list[i][1], vect_list[i][1] + vect_list[i][4])
    y_max = max(y_max, vect_list[i][1], vect_list[i][1] + vect_list[i][4])
    
    z_min = min(z_min, vect_list[i][2], vect_list[i][2] + vect_list[i][5])
    z_max = max(z_max, vect_list[i][2], vect_list[i][2] + vect_list[i][5])

margin = 0.5

ax.set_xlim([x_min - margin, x_max + margin])
ax.set_ylim([y_min - margin, y_max + margin])
ax.set_zlim([z_min - margin, z_max + margin])


plt.show()

gif_output=True

if gif_output:
    def base_to_str(base):
        base_str=f"{base}"
        base_str=base_str.replace("]\n [", ", ")
        for i in ["[", "]", "\n"]:
            base_str=base_str.replace(i, "")
        base_str=base_str.replace("  ", " ")
        return base_str

    def rotate(angle):
        ax.view_init(elev=angle)

    rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
    rot_animation.save(fr"{pathlib.Path(__file__).parent.absolute()}\Output\rotation {base_to_str(base)}.gif", dpi=120, writer='imagemagick')