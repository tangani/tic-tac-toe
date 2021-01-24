import tkinter
# import Tkinter
import numpy as np


def create_grid(event=None):
    w = c.winfo_width()    # Get current width of canvas
    h = c.winfo_height()   # Get current height of canvas
    c.delete('grid_line')  # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    count = 0
    for i in range(0, w + np.math.floor(w / 3), np.math.floor(w / 3)):
        if count <= 2:
            c.create_line([(i, 0), (i, h)], tag='grid_line')
        x_values[:, count] = i
        count += 1

    # x_values[:, count] = i + np.math.floor(w / 3))
    # print(x_values)

    # Creates all horizontal lines at intevals of 100
    count = 0
    for i in range(0, h + np.math.floor(h / 3), np.math.floor(h / 3)):
        if count <= 2:
            c.create_line([(0, i), (w, i)], tag='grid_line')
        y_values[count] = i
        count += 1

    print(y_values)


x_values = np.zeros(shape=(5, 5))
y_values = np.zeros(shape=(5, 5))

root = tkinter.Tk()

c = tkinter.Canvas(root, height=400, width=300, bg='white')
c.pack(fill=tkinter.BOTH, expand=True)

c.bind('<Configure>', create_grid)

root.mainloop()

