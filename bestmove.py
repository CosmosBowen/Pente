# read board and know situation:
# 1, check if there is one win5 -- win4 --
# 2,  check defensive/risky move

# first, read board(txt) ->
# most gathered line/column -- range<=3, in the first 3moves, no more farther than 3 lines(so no first move advantage)
# my possible moves(cordinates)= moves in range - opponent stones positison
# for each possible move, do evaluate

# function readBoard(): -> state
import math


def Alpha_Beta_Pruning(state):
    value, move = Max_Value(state, float('-inf'), float('inf'))
    return value, move


def Max_Value(state, alpha, beta):
    if is_End(state):
        return Evaluation(state)
    v = float('-inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        value, move = Min_Value(Next_State(state, action), alpha, beta)
        if value > v:
            v = value
            best_action = action
        if v >= beta:
            return v, action
        alpha = max(v, alpha)
    return v, best_action


def Min_Value(state, alpha, beta):
    if is_End(state):
        return Evaluation(state)
    v = float('inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        value, move = Max_Value(Next_State(state, action), alpha, beta)
        if value <= v:
            v = value
            best_action = action
        if v <= alpha:
            return v, action
        beta = min(v, beta)
    return v, best_action


def is_End(state):
    if state == 0:
        return True
    else:
        return False


def Actions(state):
    actions = []
    return actions


def Next_State(state, action):
    # state[9][0] = action
    return state


def Evaluation(state):
    total_eval = 0
    current_counter = {"capture": 2, "win-line": 1}
    weights = {}
    weights["capture"] = 3
    weights["win-line"] = 5
    total_eval = weights["capture"]*current_counter["capture"] + \
        weights["win-line"]*current_counter["win-line"]
    return total_eval


def read_one_line_number(line) -> tuple:
    number_list = tuple()
    number_text = ''
    for note in line:
        # print("* note ", note)
        if note == ' ':
            if number_text != '':
                number = int(number_text)
                number_list = number_list + (number,)
                number_text = ''
        else:
            number_text = number_text + note
    number = int(number_text)
    number_list = number_list + (number,)
    return number_list


# row check
def check_consecutive_row_3(row, symbol):
    count = 0
    for i in range(W - 2):
        if i == 0:
            if row[i] == symbol and row[i+1] == symbol and row[i+2] == symbol and row[i+3] != symbol:
                count += 1
                # return True
        elif i == (W-3):
            if row[i] == symbol and row[i+1] == symbol and row[i+2] == symbol and row[i-1] != symbol:
                count += 1
                # return True
        else:
            if row[i] == symbol and row[i+1] == symbol and row[i+2] == symbol and row[i+3] != symbol and row[i-1] != symbol:
                count += 1
                # return True
    return count
    # return False


def check_consecutive_row_2(row, symbol):
    count = 0
    for i in range(W-1):
        print(row[i])
        if i == 0:
            if row[i] == symbol and row[i+1] == symbol and row[i+2] != symbol:
                count += 1
                print("found it!")
                # return True
        elif i == (W-2):
            if row[i] == symbol and row[i+1] == symbol and row[i-1] != symbol:
                count += 1
                print("found it!")
                # return True
        else:
            if row[i] == symbol and row[i+1] == symbol and row[i-1] != symbol and row[i+2] != symbol:
                count += 1
                print("found it!")
                # return True
    return count
    # return False


def check_consecutive_row(number, row, symbol):
    count = 0
    for i in range(W - (number-1)):
        print(row[i])
        check = False
        for j in range(number):
            check = (row[i+j] == symbol)
            if check == False:
                break
        # check true: continue to check line starts from this letter
        # check false : this row starts from this one, no, so continue next letter(still on the same row)
        if check == False:
            continue
        if i == 0:
            if row[i+number] != symbol:
                print("found it!", "<", number, ">")
                count += 1
        elif i == (W-number):
            if row[i-1] != symbol:
                print("found it!", "<", number, ">")
                count += 1
        else:
            if row[i+number] != symbol and row[i-1] != symbol:
                print("found it!", "<", number, ">")
                count += 1
    return count


def Feature_in_a_row(board, symbol):
    row_counter = 0
    total_row_2 = 0
    total_row_3 = 0
    total_row_4 = 0
    total_row_5 = 0
    for row in board:
        print("\n--- row "+str(row_counter)+" ---")
        print(row)
        # count_3 = check_consecutive_row(3, row, symbol)
        # # count_3 = check_consecutive_row_3(row, symbol)
        # if count_3 > 0:
        #     print("check_row_3:", count_3)
        #     total_row_3 += count_3
        # count_4 = check_consecutive_row(4, row, symbol)
        # # count_3 = check_consecutive_row_3(row, symbol)
        # if count_4 > 0:
        #     print("check_row_4:", count_4)
        #     total_row_4 += count_4
        count_5 = check_consecutive_row(5, row, symbol)
        # count_3 = check_consecutive_row_3(row, symbol)
        if count_5 > 0:
            print("check_row_4:", count_5)
            total_row_5 += count_5
        # count_2 = check_consecutive_row(2, row, symbol)
        # # count_2 = check_consecutive_row_2(row, symbol)
        # if count_2 > 0:
        #     print("check_row_2:", count_2)
        #     total_row_2 += count_2
        row_counter += 1
    print("total_row_2:", total_row_2)
    print("total_row_3:", total_row_3)
    print("total_row_4:", total_row_4)
    print("total_row_5:", total_row_5)
# column check


def check_consecutive_column_2(board, symbol):
    count_total = 0
    for idx_column in range(W):
        count_each_column = 0
        print("column:", idx_column)
        for idx_row in range(H-1):
            print(board[idx_row][idx_column])
            if idx_row == 0:
                if board[idx_row][idx_column] == symbol and board[idx_row+1][idx_column] == symbol and board[idx_row+2][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1
                    # return True
            elif idx_row == (H-2):
                if board[idx_row][idx_column] == symbol and board[idx_row+1][idx_column] == symbol and board[idx_row-1][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1
                    # return True
            else:
                if board[idx_row][idx_column] == symbol and board[idx_row+1][idx_column] == symbol and board[idx_row-1][idx_column] != symbol and board[idx_row+2][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1
                    # return True

        count_total += count_each_column
        print("--", count_each_column, count_total)

    return count_total


def check_consecutive_column(number, board, symbol):
    count_total = 0
    for idx_column in range(W):
        count_each_column = 0
        print("column:", idx_column)
        for idx_row in range(H-(number-1)):
            print(board[idx_row][idx_column])
            check = False
            for i in range(number):
                check = (board[idx_row+i][idx_column] == symbol)
                if check == False:
                    break
            # check true: continue to check this column
            # check false : this column, no
            if check == False:
                continue
            if idx_row == 0:
                if board[idx_row+number][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1
            elif idx_row == (H-number):
                if board[idx_row-1][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1
            else:
                if board[idx_row+number][idx_column] != symbol and board[idx_row-1][idx_column] != symbol:
                    print("found it!")
                    count_each_column += 1

        count_total += count_each_column
        print("--", count_each_column, count_total)
    return count_total


def Feature_in_a_column(board, symbol):
    count_2 = check_consecutive_column(2, board, symbol)
    # count_2 = check_consecutive_column_2(board, symbol)
    if count_2 > 0:
        print("count_column_2:", count_2)
    count_3 = check_consecutive_column(3, board, symbol)
    if count_3 > 0:
        print("check_column_3:", count_3)


def test_check_consecutive_diagonal(number, row, symbol):
    count = 0
    for i in range(W - (number-1)):
        print(row[i])
        check = False
        for j in range(number):
            check = (row[i+j] == symbol)
            if check == False:
                break
        # check true: continue to check line starts from this letter
        # check false : this row starts from this one, no, so continue next letter(still on the same row)
        if check == False:
            continue
        if i == 0:
            if row[i+number] != symbol:
                print("found it!", "<", number, ">")
                count += 1
        elif i == (W-number):
            if row[i-1] != symbol:
                print("found it!", "<", number, ">")
                count += 1
        else:
            if row[i+number] != symbol and row[i-1] != symbol:
                print("found it!", "<", number, ">")
                count += 1
    return count


def check_consecutive_diagonal_LR(number, board, symbol):
    upper_count = 0

    start_x = 0
    print("diagonal upper:")
    # upper right corner, doesn't count for check more than 2
    for start_y in range(1, W-(number-1)):
        # start_y = 4
        # x = start_x
        y = start_y
        sub_count = 0
        print("\nstart_x:", start_x, "start_y:", start_y)
        print("diagonal--", y)
        for x in range(start_x, H):
            if x < H and y < W:
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                    print("sub_count:", sub_count)
                y += 1
        upper_count += sub_count
        print("upper_count:", upper_count)
        print()

    print("diagonal upper count_total_:", upper_count)

    lower_count = 0
    start_y = 0
    print()
    print("diagonal lower:")
    # lower left corner, doesn't count for check more than 2
    for start_x in range(H-(number-1)):
        x = start_x
        # y = start_y
        sub_count = 0
        print("\nstart_x:", start_x, "start_y:", start_y)
        print("diagonal--", x)
        for y in range(start_y, W):
            if x < H and y < W:
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                    print("sub_count:", sub_count)
                x += 1
        lower_count += sub_count
        print("lower_count:", lower_count)
        print()

    print("diagonal upper count_total_:", lower_count)
    count_total = lower_count+upper_count
    print("total:", count_total)
    return count_total


def check_consecutive_diagonal_RL(number, board, symbol):
    upper_count = 0

    start_y = 0
    print("diagonal upper:")
    # upper right corner, doesn't count for check more than 2
    for start_x in range((number-1), H):
        # start_y = 4
        # x = start_x
        x = start_x
        sub_count = 0
        print("\nstart_x:", start_x, "start_y:", start_y)
        print("diagonal--", x)
        for y in range(start_y, W):
            if x > (number-2) and y < W:
                # print("x:", x, "y:", y)
                # print("board:", board[x][y])
                if count_each_diagonal_RL(x, y, number, board, symbol):
                    sub_count += 1
                    print("sub_count:", sub_count)
                x -= 1
        upper_count += sub_count
        print("upper_count:", upper_count)
        print()

    # print("diagonal upper count_total_:", upper_count)

    lower_count = 0
    start_x = H-1
    print()
    print("diagonal lower:")
    # lower left corner, doesn't count for check more than 2
    for start_y in range(1, W-(number-1)):
        # x = start_x
        y = start_y

        sub_count = 0
        print("\nstart_x:", start_x, "start_y:", start_y)
        print("diagonal--", y)
        for x in range(start_x, 0, -1):
            if x > (number-2) and y < W:
                # print("x:", x, "y:", y)
                # print("board:", board[x][y])
                if count_each_diagonal_RL(x, y, number, board, symbol):
                    sub_count += 1
                    print("sub_count:", sub_count)
                y += 1
        lower_count += sub_count
        print("lower_count:", lower_count)
        print()

    print("diagonal lower count_total_:", lower_count)
    count_total = lower_count+upper_count
    print("total:", count_total)
    return count_total


def count_each_diagonal_RL(x, y, number, board, symbol):
    # process
    # print("x:", x, " y:", y)
    print(board[x][y], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = board[x-(num+1)][y+num+1]

    except IndexError:
        print("out of index")
    else:
        # if board[x][y] == symbol and result == symbol:
        Check_one = (board[x][y] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            # ?22?
            # potential consecutive 2, but need further check
            # print("Yes!!! ")
            # if doesn't have end, it's okay, but if there's end, has to check end is not symbol
            check_value_front = False
            if (x+1) > (H-1) or (y-1) < 0:
                # _22?
                # no symbol in front of the consecutive 2s, so the front end satisfies
                print("no value_front")
                check_value_front = True
            else:
                if board[x+1][y-1] != symbol:
                    check_value_front = True
                    # 122?
                    # the front end of consecutive satisfies, different letter
                    print("check_value_front")
                else:
                    check_value_front = False
                    print("WRONG value_front")
            if check_value_front == False:
                # y += 1
                # continue
                return False
            else:
                check_value_end = False
                if (x-number) < 0 or (y+number) > (W-1):
                    print("no value_end")
                    check_value_end = True
                else:
                    if board[x-number][y+number] != symbol:
                        check_value_end = True
                        # 1221
                        # check the end is not in the row with consecutive 2s
                        print("check_value_end")
                    else:
                        check_value_end = False
                        print("WRONG value_end")
                if check_value_end == False:
                    # y += 1
                    # continue
                    return False
                else:
                    print("found it!")
                    return True
    return False


def count_each_diagonal_LR(x, y, number, board, symbol):
    # process
    # print("x:", x, " y:", y)
    print(board[x][y], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = board[x+num+1][y+num+1]

    except IndexError:
        print("out of index")
    else:
        # if board[x][y] == symbol and result == symbol:
        Check_one = (board[x][y] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            # ?22?
            # potential consecutive 2, but need further check
            # print("Yes!!! ")
            # if doesn't have end, it's okay, but if there's end, has to check end is not symbol
            check_value_front = False
            if (x-1) < 0 or (y-1) < 0:
                # _22?
                # no symbol in front of the consecutive 2s, so the front end satisfies
                # print("no value_front")
                check_value_front = True
            else:
                if board[x-1][y-1] != symbol:
                    check_value_front = True
                    # 122?
                    # the front end of consecutive satisfies, different letter
                    # print("check_value_front")
                else:
                    check_value_front = False
                    # print("WRONG value_front")
            if check_value_front == False:
                # y += 1
                # continue
                return False
            else:
                check_value_end = False
                try:
                    value_end = board[x+number][y+number]
                except IndexError:
                    # 122_
                    # no end number of consecutive 2s, so it counts that it's complete consecutive 2s
                    # print("no value_end")
                    check_value_end = True
                else:
                    if value_end != symbol:
                        check_value_end = True
                        # 1221
                        # check the end is not in the row with consecutive 2s
                        # print("check_value_end")
                    else:
                        check_value_end = False
                        # print("WRONG value_end")
                finally:
                    if check_value_end == False:
                        # y += 1
                        # continue
                        return False
                    else:
                        print("found it!")
                        return True
    return False


Num_Row = 5
H = Num_Row
Num_Column = 7
W = Num_Column
# static
board = [
    [1, 2, 1, 2, 2, 1, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [1, 2, 2, 2, 2, 2, 2],
    [0, 2, 2, 2, 0, 1, 2]
]
board2 = [
    [1, 2, 2, 2, 2, 0, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2],
    [2, 2, 0, 1, 1, 1, 1]
]
# def Read_Board(board_notation):

player = 1
opponent = 2
print("hi, Pente")
diagonal_res = check_consecutive_diagonal_RL(4, board2, opponent)
print("**", diagonal_res)


# Feature_in_a_row(board, opponent)
# Feature_in_a_column(board, opponent)
# Feature_in_a_row(board, opponent)
# a = [1, 2, 3]
# for i in range(4):
#     try:
#         # Code that might raise an exception
#         value = a[i]
#     except IndexError:
#         # Code to handle the exception
#         print("Error: division by zero")
#     else:
#         # Code to execute if no exceptions are raised
#         print("else:", value)
#     finally:
#         # Code to execute regardless of whether an exception is raised
#         print("continue")
