import matplotlib.pyplot as plt
from math import sqrt, pi, cos, sin
from itertools import combinations
from PIL import Image
import numpy as np


def getNails(x, y, num, r):
    points = []
    step = 2 * pi / num

    def f(theta):
        return cos(theta) * r, sin(theta) * r

    theta = 0
    for i in range(num):
        points.append(f(theta))
        theta += step

    return points

points = getNails(0,0,120,12)

strings = list(combinations(points, 2))

vectors = []

for i in range(len(strings)):
    fig = plt.figure(figsize=(5,5))
    s = strings[i]
    plt.xlim(-12, 12)
    plt.ylim(-12, 12)
    plt.axis("off")
    plt.plot([s[0][0],s[1][0]], [s[0][1], s[1][1]], "-", linewidth=1.0, alpha=0.1, color="black")
    # plt.savefig(f"temp.jpeg")
    plt.close(fig)

    fig.canvas.draw()
    im = np.array(fig.canvas.renderer.buffer_rgba())
    arr = im[:, :, 0]  # Convert to grayscale
    arr = arr.reshape((arr.size, 1))

    f = np.vectorize(lambda x: int(x<240)*-20)
    vectors.append(f(arr))

# with open("strings120.npy", "rb") as f:
#     vectors = np.load(f)

a = np.concatenate(vectors, axis=1)
target = Image.open("wolverine.png").convert("L")
b = np.asarray(target)
b = b.reshape((b.size, 1))
sol = np.linalg.pinv(a).dot(b - (255 * np.ones((250000, 1))))

f = np.vectorize(lambda x: int(int(x > 0) * round(x)))
sol = (f(sol))

coeffs = list(list(sol.reshape(1, sol.size))[0])

fig = plt.figure(figsize=(5,5))

for s, c in zip(strings, coeffs):
    plt.xlim(-12, 12)
    plt.ylim(-12, 12)
    plt.axis("off")
    for i in range(c):
        plt.plot([s[0][0],s[1][0]], [s[0][1], s[1][1]], "-", linewidth=1.0, alpha=0.1, color="black")

plt.savefig(f"final.jpeg")
plt.show()

