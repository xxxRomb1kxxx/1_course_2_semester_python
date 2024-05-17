import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = np.linspace(0, 2 * np.pi, 1000)
    a = frame / 100
    b = 1
    x = np.sin(a * t)
    y = np.sin(b * t)
    line.set_data(x, y)
    ax.set_title(f'Lissajous Figure (a={a:.2f}, b={b})')
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), init_func=init, blit=True)

plt.show()