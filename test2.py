import numpy as np

ratios = np.array([2, 1, 0.5])
w, h, x_ctr, y_ctr = 16, 16, 7.5, 7.5
size = w * h
size_ratios = size / ratios

ws = np.round(np.sqrt(size_ratios))
hs = np.round(ws * ratios)

print(size, size_ratios, ws, hs)

