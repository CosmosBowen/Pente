def get_board_and_args(board_size):
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    # 'ME':1
    # 'OPPONENT':2
    # board_size = 19
    W = board_size
    H = board_size
    board = [[0 for _ in range(W)] for _ in range(H)]
    i = 0
    with open('./input.txt') as f:
        for line in f:
            line = line.strip()
            i = i + 1
            if i == 1:
                player_color = line
            elif i == 2:
                time_left = float(line)
            elif i == 3:
                catch_count = [0, 0]
                line = line.split(",")
                catch_count[0] = line[0]
                catch_count[1] = line[1]
            else:
                # print("line<", i, ">")
                for idx, stone in enumerate(line):

                    if stone != ".":
                        # print("HA")
                        # print(idx, ",", stone)
                        if stone == "w":
                            if player_color == BLACK:
                                board[i-4][idx] = 2
                            else:
                                board[i-4][idx] = 1
                        elif stone == "b":
                            if player_color == BLACK:
                                board[i-4][idx] = 1
                            else:
                                board[i-4][idx] = 2
                        else:
                            pass
    return (board, player_color, time_left)
