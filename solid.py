import numpy as np
from stl import mesh

def f(x):
    return 2 + np.sin(x)

N = 15
M = 12
SCALE = 1 / 10

x_vals = np.linspace(0, 2 * np.pi, N)
theta_vals = np.linspace(0, np.pi/2, M)
y_vals = f(x_vals)


vertices = []
faces = []

def joinFour(a, b, c, d):
    faces.append([a, b, c])
    faces.append([a, c, d])

def joinThree(a, b, c):
    faces.append([a, b, c])

for z, y in enumerate(y_vals):
    # make N points along the semi circle
    # center at [z * SCALE, y / 2, 0]
    ind = len(vertices)

    # put in the center
    vertices.append([z * SCALE, 0, 0])

    for theta in theta_vals:
        vertices.append([z * SCALE, y/2 * np.cos(theta), (y/2 * np.sin(theta))])

    # faces with the center
    for i in range(1, M):
        joinThree(ind, ind+i, ind+i+1)
    
    # faces with the previous one
    if z == 0:
        continue

    pv = ind-M-1

    for i in range(1, M):
        joinFour(ind+i, ind+i+1, pv+i+1, pv+i)

    # the floor
    joinFour(ind, ind+1, pv+1, pv)
    
    # the wall
    joinFour(ind, ind+M, pv+M, pv)


vertices = np.array(vertices)
faces = np.array(faces)

solid = mesh.Mesh(np.zeros(faces.shape[0], dtype = mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        solid.vectors[i][j] = vertices[f[j], :]

solid.save('calculus_solid.stl')