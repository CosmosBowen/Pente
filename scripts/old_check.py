H = W = 8


def count_each_row(x, number, row, symbol):
    print(row[x], end=" ")
    try:
        result = [None]*(number-1)
        for num in range(number-1):
            result[num] = row[x+num+1]

    except IndexError:
        print("out of index")
        # end
        # pass

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
                print("no value_front")
                check_value_front = True
            else:
                if row[x-1] != symbol:
                    # check_value_front
                    print("check_value_front")
                    check_value_front = True
                else:
                    # WRONG value_front
                    print("WRONG value_front")
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                try:
                    value_end = row[x+number]
                except IndexError:
                    print("no value_end")
                    # no value_end
                    check_value_end = True
                else:
                    if value_end != symbol:
                        # check_value_end
                        print("check_value_end")
                        check_value_end = True
                    else:
                        print("WRONG value_end")
                        # WRONG value_end
                        check_value_end = False
                finally:
                    if check_value_end == False:
                        return False
                    else:
                        print("found it!")
                        # found it!
                        return True

    return False


def check_consecutive_row(number, board, symbol):
    # count = 0
    # for row in board:
    #     sub_count = check_consecutive_each_row(number, row, symbol)
    #     count_each_row
    #     if sub_count > 0:
    #         count += sub_count
    # return count

    row_counter = 0
    this_row_count = 0

    for row in board:
        print("\n--row-- ", row_counter)
        sub_count = 0
        for x in range(W-(number-1)):

            if count_each_row(x, number, row, symbol):
                sub_count += 1
        this_row_count += sub_count
        row_counter += 1
    return this_row_count


def check_consecutive_diagonal_LR(number, board, symbol):
    upper_count = 0

    start_x = 0
    for start_y in range(1, W-(number-1)):
        y = start_y
        sub_count = 0
        for x in range(start_x, H):
            if x < H and y < W:
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                y += 1
        upper_count += sub_count

    lower_count = 0
    start_y = 0
    for start_x in range(H-(number-1)):
        x = start_x
        sub_count = 0
        for y in range(start_y, W):
            if x < H and y < W:
                if count_each_diagonal_LR(x, y, number, board, symbol):
                    sub_count += 1
                x += 1
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
            if (x-1) < 0 or (y-1) < 0:
                # no value_front
                check_value_front = True
            else:
                if board[x-1][y-1] != symbol:
                    # check_value_front
                    check_value_front = True
                else:
                    # WRONG value_front
                    check_value_front = False
            if check_value_front == False:
                return False
            else:
                check_value_end = False
                try:
                    value_end = board[x+number][y+number]
                except IndexError:
                    # no value_end
                    check_value_end = True
                else:
                    if value_end != symbol:
                        # check_value_end
                        check_value_end = True
                    else:
                        # WRONG value_end
                        check_value_end = False
                finally:
                    if check_value_end == False:
                        return False
                    else:
                        # found it!
                        return True
    return False
