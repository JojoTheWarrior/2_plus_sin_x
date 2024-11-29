import numpy as np
from stl import mesh

def f(x):
    return 2 + np.sin(x)

N = 50

x_vals = np.linspace(0, 2 * np.pi, N)
y_vals = f(x_vals)


vertices = []
faces = []

for y in y_vals:
