import sys
import math
import copy


Num_Row = 3  # 5
H = Num_Row
Num_Column = 3  # 7
W = Num_Column
# static
player = 1
opponent = 2


def Alpha_Beta_Pruning(state, depth):
    print("DEPTH(Alpha_Beta_Pruning):", depth)
    value, move = Max_Value(state, float('-inf'), float('inf'), depth)
    return value, move


def Max_Value(state, alpha, beta, depth):
    print("DEPTH(Max_Value):", depth)
    if depth == 0:
        return Evaluation(state, opponent)
    # if is_End(state):
    #     print("Max_Value isEnd")
    #     return Evaluation(state, player)
    v = float('-inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        print("\naction:", action)
        next_state = Next_State(state, action, player)
        print("next_state:")
        for sub_state in next_state:
            print(sub_state)
        move = action
        value = 0
        res = Min_Value(next_state, alpha, beta, depth-1)
        try:
            value = res[0]
            move = res[1]
        except TypeError:
            value = res
            # pass
        finally:
            # print("value:", value, " move:", move)
            if value > v:
                v = value
                best_action = action
            if v >= beta:
                return v, action
            alpha = max(v, alpha)
    return v, best_action


def Min_Value(state, alpha, beta, depth):
    print("DEPTH(Min_Value):", depth)
    if depth == 0:
        res = Evaluation(state, player)
        print("Min_Evaluation:", res)
        return res
        # return Evaluation(state, opponent)
    # if is_End(state):
    #     return Evaluation(state, opponent)
    v = float('inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        move = action
        value = 0
        res = Max_Value(Next_State(
            state, action, opponent), alpha, beta, depth-1)
        try:
            value = res[0]
            move = res[1]
        except TypeError:
            value = res
            # pass
        finally:
            # print("value:", value, " move:", move)
            if value < v:
                v = value
                best_action = action
            if v <= alpha:
                return v, action
            beta = min(v, beta)
    return v, best_action


def Actions(state):
    actions = []
    for y in range(W):
        for x in range(H):
            if state[x][y] == 0:
                actions.append((x, y))
    # print("actions:", actions)
    return actions


def Next_State(state, action, who):
    who = player
    if who == opponent:
        who = opponent
    new_state = copy.deepcopy(state)
    new_state[action[0]][action[1]] = who
    return new_state


def count_each_row(x, number, row, symbol):
    # print(row[x], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = row[x+num+1]

    except IndexError:
        # print("out of index")
        pass

    else:
        Check_one = (row[x] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            check_value_front = False
            if (x-1) < 0:
                # no value_front
                # print("no value_front")
                check_value_front = True
            else:
                if row[x-1] != symbol:
                    # check_value_front
                    # print("check_value_front")
                    check_value_front = True
                else:
                    # WRONG value_front
                    # print("WRONG value_front")
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                try:
                    value_end = row[x+number]
                except IndexError:
                    # print("no value_end")
                    # no value_end
                    check_value_end = True
                else:
                    if value_end != symbol:
                        # check_value_end
                        # print("check_value_end")
                        check_value_end = True
                    else:
                        # print("WRONG value_end")
                        # WRONG value_end
                        check_value_end = False
                finally:
                    if check_value_end == False:
                        return False
                    else:
                        # print("found it!")
                        # found it!
                        return True
    return False


def check_consecutive_row(number, board, symbol):
    # row_counter = 0
    this_row_count = 0

    for row in board:
        # print("\n--row-- ", row_counter)
        sub_count = 0
        for x in range(W-(number-1)):
            if count_each_row(x, number, row, symbol):
                sub_count += 1
        this_row_count += sub_count
        # row_counter += 1
    return this_row_count


def count_each_column(x, y, number, board, symbol):
    # print(board[x][y], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = board[x+num+1][y]

    except IndexError:
        pass
        # print("out of index")
    else:
        Check_one = (board[x][y] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            check_value_front = False
            if (x-1) < 0:
                # no value_front
                # print("no value_front")
                check_value_front = True
            else:
                if board[x-1][y] != symbol:
                    # check_value_front
                    # print("check_value_front")
                    check_value_front = True
                else:
                    # WRONG value_front
                    # print("WRONG value_front")
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                try:
                    value_end = board[x+number][y]
                except IndexError:
                    # no value_end
                    # print("no value_end")
                    check_value_end = True
                else:
                    if value_end != symbol:
                        # check_value_end
                        # print("check_value_end")
                        check_value_end = True
                    else:
                        # WRONG value_end
                        # print("WRONG value_end")
                        check_value_end = False
                finally:
                    if check_value_end == False:
                        return False
                    else:
                        # found it!
                        # print("found it!")
                        return True
    return False


def check_consecutive_column(number, board, symbol):
    total_count = 0
    for y in range(W):
        # for each column
        # print("\n--column-- ", y)
        sub_count = 0
        for x in range(H-(number-1)):
            if count_each_column(x, y, number, board, symbol):
                sub_count += 1
        total_count += sub_count
        # print("sub_count: ", sub_count)

    return total_count


def check_consecutive_diagonal_LR(number, board, symbol):  # \
    upper_count = 0

    start_x = 0
    for start_y in range(1, W-(number-1)):
        # print("\n--diagonal-- ", start_y)
        y = start_y
        sub_count = 0
        for x in range(start_x, H):
            if x < H-(number-1) and y < W-(number-1):
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                y += 1
        # print("\nsub_count:", sub_count)
        upper_count += sub_count

    lower_count = 0
    start_y = 0
    # print("\n*************\n")
    for start_x in range(H-(number-1)):
        # print("\n--diagonal-- ", start_x)
        x = start_x
        sub_count = 0
        for y in range(start_y, W):
            if x < H-(number-1) and y < W-(number-1):
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                x += 1
        # print("\nsub_count:", sub_count)
        lower_count += sub_count

    count_total = lower_count+upper_count
    return count_total


def count_each_diagonal_LR(x, y, number, board, symbol):
    # print(board[x][y], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = board[x+num+1][y+num+1]

    except IndexError:
        # print("out of index")
        pass
    else:
        Check_one = (board[x][y] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            check_value_front = False
            if (x-1) < 0 or (y-1) < 0:
                # no value_front
                # print("no value_front")
                check_value_front = True
            else:
                if board[x-1][y-1] != symbol:
                    # check_value_front
                    # print("check_value_front")
                    check_value_front = True
                else:
                    # WRONG value_front
                    # print("WRONG value_front")
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                try:
                    value_end = board[x+number][y+number]
                except IndexError:
                    # no value_end
                    # print("no value_end")
                    check_value_end = True
                else:
                    if value_end != symbol:
                        # check_value_end
                        # print("check_value_end")
                        check_value_end = True
                    else:
                        # WRONG value_end
                        # print("WRONG value_end")
                        check_value_end = False
                finally:
                    if check_value_end == False:
                        return False
                    else:
                        # found it!
                        # print("found it!")
                        return True
    return False


def check_consecutive_diagonal_RL(number, board, symbol):  # /
    upper_count = 0

    start_y = 0
    # diagonal upper
    for start_x in range((number-1), H):
        # print("\n--diagonal-- ", start_x)
        x = start_x
        sub_count = 0
        for y in range(start_y, W):
            if x > (number-2) and y < W-(number-1):  # y < W-(number-1)
                if count_each_diagonal_RL(x, y, number, board, symbol):
                    sub_count += 1
                x -= 1
        # print("\nsub_count:", sub_count)
        upper_count += sub_count

    lower_count = 0
    start_x = H-1
    # print("\n*************\n")
    for start_y in range(1, W-(number-1)):
        # print("\n--diagonal-- ", start_y)
        y = start_y
        sub_count = 0
        for x in range(start_x, 0, -1):
            if x > (number-2) and y < W-(number-1):
                if count_each_diagonal_RL(x, y, number, board, symbol):
                    sub_count += 1
                y += 1
        # print("\nsub_count:", sub_count)
        lower_count += sub_count

    count_total = lower_count+upper_count
    return count_total


def count_each_diagonal_RL(x, y, number, board, symbol):
    # print(board[x][y], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = board[x-(num+1)][y+num+1]
    except IndexError:
        pass
        # print("out of index")
    else:
        Check_one = (board[x][y] == symbol)
        Check_two = True
        for res in result:
            if res != symbol:
                Check_two = False
                break
        if Check_one and Check_two:
            check_value_front = False
            if (x+1) > (H-1) or (y-1) < 0:
                # no value_front
                # print("no value_front")
                check_value_front = True
            else:
                if board[x+1][y-1] != symbol:
                    # check_value_front
                    # print("check_value_front")
                    check_value_front = True
                else:
                    # WRONG value_front
                    # print("WRONG value_front")
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                if (x-number) < 0 or (y+number) > (W-1):
                    # no value_end
                    # print("no value_end")
                    check_value_end = True
                else:
                    if board[x-number][y+number] != symbol:
                        # check_value_end
                        # print("check_value_end")
                        check_value_end = True
                    else:
                        # WRONG value_end
                        # print("WRONG value_end")
                        check_value_end = False
                if check_value_end == False:
                    return False
                else:
                    # found it!
                    # print("found it!")
                    return True
    return False


def count_consecutive(number, board, symbol):
    total = 0
    count_row = check_consecutive_row(number, board, symbol)
    count_column = check_consecutive_column(number, board, symbol)
    count_diagonal_LR = check_consecutive_diagonal_LR(number, board, symbol)
    count_diagonal_RL = check_consecutive_diagonal_RL(number, board, symbol)
    total = count_row+count_column+count_diagonal_LR+count_diagonal_RL
    return total


def Evaluation(board, symbol):
    total_eval = 0
    weights = {"me-2-in-line": 1, "win-line": 100}
    count_2 = count_consecutive(2, board, symbol)
    count_3 = count_consecutive(3, board, symbol)
    current_counter = {"me-2-in-line": count_2, "win-line": count_3}
    for name, weight in weights.items():
        total_eval += weight*current_counter[name]
    return total_eval


board = [
    [1, 1, 1, 0, 2, 1, 1],
    [1, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 2, 1, 1, 2]
]

board_tic = [
    [2, 0, 0],
    [1, 0, 1],
    [0, 0, 2]
]
# board_tic = [
#     [0, 1, 0],
#     [2, 1, 2],
#     [0, 0, 0]
# ]


res = Alpha_Beta_Pruning(board_tic, 1)
print("res:", res)
