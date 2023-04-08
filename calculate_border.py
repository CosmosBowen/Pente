board_size = 10
W = board_size
H = board_size
stretch_length = 1

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def get_range_column_start_idx():
    for i in range(W):
        for j in range(H):
            if board[j][i] != 0:
                # print("column start", i)
                return i


range_column_start_idx = get_range_column_start_idx()


def get_range_column_end_idx():
    for i in reversed(range(W)):
        for j in range(H):
            if board[j][i] != 0:
                # print("column end", i)
                return i


range_column_end_idx = get_range_column_end_idx()

print("column:", range_column_start_idx, ",", range_column_end_idx)

range_row_start_idx = 0
for i in range(H):
    count_1 = board[i].count(1)
    count_2 = board[i].count(2)
    count_total = count_1+count_2
    if count_total > 0:
        range_row_start_idx = i
        # print("row start", i, count_total)
        break

range_row_end_idx = 0
for i in reversed(range(H)):
    count_1 = board[i].count(1)
    count_2 = board[i].count(2)
    count_total = count_1+count_2
    if count_total > 0:
        range_row_end_idx = i
        # print("row end", i, count_total)
        break

print("row:", range_row_start_idx, ",", range_row_end_idx)


def print_border():
    for i in range(range_row_start_idx, range_row_end_idx+1):
        for j in range(range_column_start_idx, range_column_end_idx+1):
            print(board[i][j], end=" ")
        print()


def define_extended_border():
    # stretch_length = 1
    row_start = max(0, range_row_start_idx-stretch_length)
    row_end = min(H-1, range_row_end_idx+stretch_length)
    column_start = max(0, range_column_start_idx-stretch_length)
    column_end = min(W-1, range_column_end_idx+stretch_length)
    for i in range(row_start, row_end+1):
        for j in range(column_start, column_end+1):
            print(board[i][j], end=" ")
        print()


def Actions():
    actions = []
    # stretch_length = 1
    row_start = max(0, range_row_start_idx-stretch_length)
    row_end = min(H-1, range_row_end_idx+stretch_length)
    column_start = max(0, range_column_start_idx-stretch_length)
    column_end = min(W-1, range_column_end_idx+stretch_length)
    for i in range(row_start, row_end+1):
        for j in range(column_start, column_end+1):
            if board[i][j] == 0:
                actions.append((i, j))
    return actions


print_border()
print()
define_extended_border()
actions = Actions()
print(actions)

# def Actions():
