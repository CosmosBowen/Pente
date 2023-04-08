import numpy as np

size = 5-1
board = [
    [4, 0, 0, 0, 8],
    [0, 0, 5, 0, 7],
    [2, 0, 4, 5, 6],
    [1, 0, 1, 0, 0],
    [0, 1, 2, 3, 4],
]
# create a 2D array
arr = np.array(board)
# switch column
# b = arr[:, ::-1]
# print(b)

# diags_main = []
for diag_idx in range(-size, size+1):
    row = arr.diagonal(diag_idx)
    print(diag_idx, ":", row)
    for idx in range(len(row)):
        if row[idx] == 0:
            if diag_idx > 0:
                y = idx
                x = diag_idx+idx
            elif diag_idx < 0:
                y = abs(diag_idx)+idx
                x = idx
            else:
                y = x = idx
            print(y, ",", x)

# print("diags_main:")
# for row in diags_main:
#     print(row)


# diags_opp = []
arr_opp = arr[::-1, :]
for diag_idx in range(-size, size+1):
    row = arr_opp.diagonal(diag_idx)
    print(diag_idx, ":", row)
    for idx in range(len(row)):
        if row[idx] == 0:
            if diag_idx > 0:
                y = size-idx
                x = diag_idx+idx
            elif diag_idx < 0:
                y = size+diag_idx-idx
                x = idx
            else:
                y = size-idx
                x = idx
            print(y, ",", x)

# print("diags_opp:")
# for row in diags_opp:
#     print(row)
