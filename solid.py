import numpy as np
from stl import mesh

def f(x):
    return 2 + np.sin(x)

N = 50
SCALE = 1 / 10

x_vals = np.linspace(0, 2 * np.pi, N)
y_vals = f(x_vals)


vertices = []
faces = []

for z, y in enumerate(y_vals):
    v0 = [SCALE * z, 0, 0]
    v1 = [SCALE * z, y, 0]
    v2 = [SCALE * z, y, y]
    v3 = [SCALE * z, 0, y]
    
    ind = len(vertices)
    vertices.extend([v0, v1, v2, v3])

    # same face
    faces.append([ind, ind+1, ind+2])
    faces.append([ind, ind+2, ind+3])

    # with past face
    if z == 0: 
        continue
    # far
    faces.append([ind+1, ind+2, ind-2])
    faces.append([ind+1, ind-2, ind-3])
    # near
    faces.append([ind, ind+3, ind-1])
    faces.append([ind, ind-1, ind-4])
    # top
    faces.append([ind+3, ind+2, ind-2])
    faces.append([ind+3, ind-2, ind-1])
    # bottom
    faces.append([ind, ind+1, ind-3])
    faces.append([ind, ind-3, ind-4])

vertices = np.array(vertices)
faces = np.array(faces)

solid = mesh.Mesh(np.zeros(faces.shape[0], dtype = mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        solid.vectors[i][j] = vertices[f[j], :]

solid.save('calculus_solid.stl')