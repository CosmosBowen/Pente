class AI_agent:
    def __init__(self) -> None:
        self.opponent_move = 6

    def AI_best_move(self, board, time_left):
        # check winning spot z(oooo_)
        
        # check lose spot z(oxxxx_ / _xx_x_ / _xxx_)
        self.opponent_move += 1
        return (self.opponent_move, 'B')
