from scripts.check_winning_spot import check_winning_spot
BOARD_SIZE = 19
H = W = BOARD_SIZE
# AI : 2


def AI_best_move(board, time_left):
    # check winning spot z(2222_)
    res = check_winning_spot(board)
    if res != False:
        return (res,True)
    else:
        pass

    # check lose spot z(21111_ / _11_1_ / _111_)
