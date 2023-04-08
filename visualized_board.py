# H=3
# W=3

# board=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0],
# ]

# import matplotlib.pyplot as plt

# # create a 19x19 board (Go board size)
# board_size = 19
# board = [[0 for x in range(board_size)] for y in range(board_size)]

# # set some stones on the board for visualization
# board[5][5] = 1  # black stone
# board[7][10] = 2  # white stone

# # plot the board
# plt.imshow(board, cmap='binary', interpolation='nearest')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.colors import LogNorm

# dx, dy = 0.015, 0.05
# x = np.arange(-4.0, 4.0, dx)
# y = np.arange(-4.0, 4.0, dy)
# X, Y = np.meshgrid(x, y)
# extent = np.min(x), np.max(x), np.min(y), np.max(y)
# z1 = np.add.outer(range(8), range(8)) % 2
# plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

# def chess(x, y):
#     return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))
# z2 = chess(X, Y)
# plt.imshow(z2, alpha=0.7, interpolation="bilinear", extent=extent)
# plt.title("Chess Board with Python")
# plt.show()
