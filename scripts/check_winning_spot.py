import numpy as np
BOARD_SIZE = 19
H = W = BOARD_SIZE
SIZE = H-1
# H = W = 8
# size = H-1

# board = [
#     [0, 0, 2, 2, 2, 2, 1, 1],
#     [0, 1, 0, 2, 2, 2, 2, 0],
#     [2, 2, 2, 2, 2, 2, 0, 1],
#     [1, 2, 2, 2, 2, 2, 2, 0],
#     [0, 2, 2, 2, 2, 2, 0, 1],
#     [2, 1, 2, 2, 2, 2, 0, 0],
#     [1, 0, 2, 2, 0, 1, 0, 1],
#     [1, 1, 2, 2, 0, 1, 1, 2],
# ]


def winning_spot_row(board):
    for row_idx in range(H):
        row = board[row_idx]
        # print("row", row_idx, ":", row)
        # 1. at least more than four 2s in this row:
        rough_count = row.count(2)
        if rough_count < 4:
            continue
        else:
            # 2. find index of the first 2 in the row
            idx_start = row.index(2)
            # 3. check every iteration
            for idx in range(idx_start, W-3):
                # 4. check 22220 or 02222
                pattern_1 = row[idx:idx+5]
                pattern_2 = row[idx-1:idx+4]
                if pattern_1 == [2, 2, 2, 2, 0]:
                    y = row_idx
                    x = idx+4
                    # print("!", (y, x))
                    return (y, x)
                else:
                    if pattern_2 == [0, 2, 2, 2, 2]:
                        y = row_idx
                        x = idx-1
                        # print("!", (y, x))
                        return (y, x)
                    else:
                        continue
            # print("this row end")
    return False


def winning_spot_column(board):
    for col_idx in range(W):
        row = [each_row[col_idx] for each_row in board]
        # print("column", col_idx, ":", row)
        # 1. at least more than four 2s in this row:
        rough_count = row.count(2)
        if rough_count < 4:
            continue
        else:
            # 2. find index of the first 2 in the row
            idx_start = row.index(2)
            # 3. check every iteration
            for idx in range(idx_start, H-3):
                # 4. check 22220 or 02222
                pattern_1 = row[idx:idx+5]
                pattern_2 = row[idx-1:idx+4]
                if pattern_1 == [2, 2, 2, 2, 0]:
                    y = idx+4
                    x = col_idx
                    # print("!", (y, x))
                    return (y, x)
                else:
                    if pattern_2 == [0, 2, 2, 2, 2]:
                        y = idx-1
                        x = col_idx
                        # print("!", (y, x))
                        return (y, x)
                    else:
                        continue
            # print("this row end")
    return False


def main_coordinates_from_diagonal_to_2d(diag_idx, idx):
    if diag_idx > 0:
        y = idx
        x = diag_idx+idx
    elif diag_idx < 0:
        y = abs(diag_idx)+idx
        x = idx
    else:
        y = x = idx
    # print("!", (y, x))
    return (y, x)


def winning_spot_diagonal_main(board):
    arr = np.array(board)
    # diags_main
    range_size = W-5  # [2,2,2,2,0] or [0,2,2,2,2] has length 5
    for diag_idx in range(-range_size, range_size+1):
        row = arr.diagonal(diag_idx)
        # print("diag_main:", diag_idx, ":", row)
        # 1. at least more than four 2s in this row:
        # rough_count = row.count(2)
        rough_count = np.count_nonzero(row == 2)
        print(rough_count)
        if rough_count < 4:
            continue
        else:
            # 2. find index of the first 2 in the row
            # row.index(2)
            idx_start = np.where(row == 2)[0][0]
            # 3. check every iteration
            for idx in range(idx_start, len(row)-3):
                # 4. check 22220 or 02222
                pattern_1 = row[idx:idx+5]
                pattern_2 = row[idx-1:idx+4]
                if np.array_equal(pattern_1, np.array([2, 2, 2, 2, 0])):
                    new_idx = idx+4
                    y, x = main_coordinates_from_diagonal_to_2d(
                        diag_idx, new_idx)
                    return (y, x)
                else:
                    if np.array_equal(pattern_2, np.array([0, 2, 2, 2, 2])):
                        new_idx = idx-1
                        y, x = main_coordinates_from_diagonal_to_2d(
                            diag_idx, new_idx)
                        return (y, x)
                    else:
                        continue
            # print("this row end")
    return False


def opp_coordinates_from_diagonal_to_2d(diag_idx, idx):
    if diag_idx > 0:
        y = SIZE-idx
        x = diag_idx+idx
    elif diag_idx < 0:
        y = SIZE+diag_idx-idx
        x = idx
    else:
        y = SIZE-idx
        x = idx
    # print("!", (y, x))
    return (y, x)


def winning_spot_diagonal_opp(board):
    arr = np.array(board)
    # arr_opp
    arr = arr[::-1, :]
    # diags_opp
    range_size = W-5  # [2,2,2,2,0] or [0,2,2,2,2] has length 5
    for diag_idx in range(-range_size, range_size+1):
        row = arr.diagonal(diag_idx)
        # print("diag_opp:", diag_idx, ":", row)
        # 1. at least more than four 2s in this row:
        # rough_count = row.count(2)
        rough_count = np.count_nonzero(row == 2)
        if rough_count < 4:
            continue
        else:
            # 2. find index of the first 2 in the row
            # idx_start = row.index(2)
            idx_start = np.where(row == 2)[0][0]
            # 3. check every iteration
            for idx in range(idx_start, len(row)-3):
                # 4. check 22220 or 02222
                pattern_1 = row[idx:idx+5]
                pattern_2 = row[idx-1:idx+4]
                if np.array_equal(pattern_1, np.array([2, 2, 2, 2, 0])):
                    new_idx = idx+4
                    y, x = opp_coordinates_from_diagonal_to_2d(
                        diag_idx, new_idx)
                    return (y, x)
                else:
                    if np.array_equal(pattern_2, np.array([0, 2, 2, 2, 2])):
                        new_idx = idx-1
                        y, x = opp_coordinates_from_diagonal_to_2d(
                            diag_idx, new_idx)
                        return (y, x)
                    else:
                        continue
            # print("this row end")
    return False


def check_winning_spot(board):
    isRow = winning_spot_row(board)
    if isRow != False:
        return isRow
    else:
        isColumn = winning_spot_column(board)
        if isColumn != False:
            return isColumn
        else:
            isDiagonal_main = winning_spot_diagonal_main(board)
            if isDiagonal_main != False:
                return isDiagonal_main
            else:
                isDiagonal_opp = winning_spot_diagonal_opp(board)
                if isDiagonal_opp != False:
                    return isDiagonal_opp
                else:
                    return False


# res = check_winning_spot(board)
# print("res:", res)
