import pygame
from scripts.read_input import get_board_and_args
# from scripts.AI_agent import AI_agent
from scripts.AI_play import AI_best_move

# suppress the message of pygame initialization
# import logging
# logging.getLogger("pygame").setLevel(logging.WARNING)


# Define PenteMove: "3,A"

pygame.font.init()
# my_fonts = pygame.font.get_fonts()
# for item in my_fonts:
#     print(item)
WHITE = 'WHITE'
BLACK = 'BLACK'
PLAYER_COLOR = WHITE  # default
OPPONENT_COLOR = BLACK  # default
TIME_LEFT = 300  # default 5min

BOARD_SIZE = 19
NOTATION_FONT = pygame.font.SysFont('georgia', 15)
PADDING = 25
WIN_H = 810
WIN_W = 900  # 1000
SQUARE_SIZE = 40
STONE_SIZE = 45
LINE_WIDTH = 1
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_BOARD = (237, 198, 130)
PLACE_STONE = pygame.USEREVENT+1
LETTER = ["A", "B", "C", "D", "E", "F", "G", "H", "J",
          "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
# board = [
#     [0, 0, 1, 1],
#     [0, 2, 0, 0],
#     [2, 1, 2, 0],
#     [1, 0, 0, 2]
# ]


STONE_BLACK_IMAGE = pygame.image.load("./assets/black_stone.png")
STONE_BLACK = pygame.transform.scale(
    STONE_BLACK_IMAGE, (STONE_SIZE, STONE_SIZE))
STONE_WHITE_IMAGE = pygame.image.load("./assets/white_stone1.png")
STONE_WHITE = pygame.transform.scale(
    STONE_WHITE_IMAGE, (STONE_SIZE, STONE_SIZE))
WINDOW = pygame.display.set_mode((WIN_W, WIN_H))
# BORDER = pygame.Rect(10, 10, LINE_WIDTH, STONE_SIZE)

BOARD, PLAYER_COLOR, TIME_LEFT = get_board_and_args(BOARD_SIZE)
OPPONENT_COLOR = BLACK if PLAYER_COLOR == WHITE else WHITE
print("PLAYER_COLOR:", PLAYER_COLOR, "\nOPPONENT_COLOR:", OPPONENT_COLOR)


def print_board_representation():
    print("------------------------------")
    for row in BOARD:
        print(row)
    print("------------------------------")


print_board_representation()


def draw_stones():
    STONE_PLAYER = STONE_WHITE if PLAYER_COLOR == WHITE else STONE_BLACK
    STONE_OPPONENT = STONE_BLACK if STONE_PLAYER == STONE_WHITE else STONE_WHITE
    for idx_row in range(BOARD_SIZE):
        for idx_column in range(BOARD_SIZE):
            stone = BOARD[idx_row][idx_column]
            if stone != 0:
                if stone == 1:
                    WINDOW.blit(STONE_PLAYER, (SQUARE_SIZE*(idx_column+1) -
                                STONE_SIZE // 2+PADDING, SQUARE_SIZE*(idx_row+1)-STONE_SIZE//2+PADDING))
                if stone == 2:
                    WINDOW.blit(STONE_OPPONENT, (SQUARE_SIZE*(idx_column+1) -
                                STONE_SIZE // 2+PADDING, SQUARE_SIZE*(idx_row+1)-STONE_SIZE//2+PADDING))


def draw_borders():
    for num in range(BOARD_SIZE):
        column = pygame.Rect((num+1)*SQUARE_SIZE-LINE_WIDTH //
                             2+PADDING, SQUARE_SIZE+PADDING, LINE_WIDTH, SQUARE_SIZE*(BOARD_SIZE-1))
        row = pygame.Rect(SQUARE_SIZE-LINE_WIDTH//2+PADDING, (num+1)*SQUARE_SIZE -
                          LINE_WIDTH//2+PADDING, SQUARE_SIZE*(BOARD_SIZE-1)+LINE_WIDTH, LINE_WIDTH)
        pygame.draw.rect(WINDOW, COLOR_BLACK, row)
        pygame.draw.rect(WINDOW, COLOR_BLACK, column)


def draw_notations():
    for num in range(BOARD_SIZE):
        notation_number = NOTATION_FONT.render(
            str(BOARD_SIZE-num), 1, COLOR_BLACK)
        # row
        WINDOW.blit(notation_number, (PADDING, (num+1)*SQUARE_SIZE -
                    notation_number.get_height()//2+PADDING))
        notation_letter = NOTATION_FONT.render(LETTER[num], 1, COLOR_BLACK)
        # column
        WINDOW.blit(notation_letter, ((num+1)*SQUARE_SIZE -
                    notation_letter.get_width()//2+PADDING, PADDING))


def draw_window():
    WINDOW.fill(COLOR_BOARD)
    draw_borders()
    draw_notations()
    draw_stones()
    pygame.display.update()


def place_stone(is_player, stone_color, PenteMove):
    print(stone_color, ":", PenteMove)
    x, y = PenteMove
    stone_choice = {BLACK: STONE_BLACK, WHITE: STONE_WHITE}
    # board representation update
    update_board(BOARD, is_player, PenteMove)
    # visualize
    WINDOW.blit(stone_choice[stone_color],
                (SQUARE_SIZE*LETTER.index(y) - STONE_SIZE // 2+PADDING+SQUARE_SIZE,
                 SQUARE_SIZE*(BOARD_SIZE-x)-STONE_SIZE//2+PADDING+SQUARE_SIZE)
                )


def update_board(BOARD, is_player, PenteMove):
    x = BOARD_SIZE-PenteMove[0]
    y = LETTER.index(PenteMove[1])
    BOARD[x][y] = 1 if is_player else 2
    print_board_representation()


def get_pente_move(mouse_position):
    mouse_y = mouse_position[0]
    mouse_x = mouse_position[1]
    idx_column = round((mouse_y + STONE_SIZE //
                        2-PADDING)/SQUARE_SIZE - 1)
    idx_row = round(
        (mouse_x+STONE_SIZE//2-PADDING)/SQUARE_SIZE - 1)
    mouse_radius = 5
    rec_mouse = pygame.Rect(mouse_y-mouse_radius//2,
                            mouse_x-mouse_radius//2, mouse_radius, mouse_radius)
    # visualize rec_mouse
    # pygame.draw.rect(WINDOW, COLOR_RED, rec_mouse)

    # colision
    collide_recs = []
    idx_positions = []
    idx_positions.append((idx_row, idx_column))
    idx_positions.append((idx_row, idx_column+1))
    idx_positions.append((idx_row+1, idx_column))
    idx_positions.append((idx_row+1, idx_column+1))
    for idx_posistion in idx_positions:
        collide_recs.append((SQUARE_SIZE*idx_posistion[1] -
                            STONE_SIZE // 2+PADDING, SQUARE_SIZE*idx_posistion[0]-STONE_SIZE//2+PADDING, STONE_SIZE, STONE_SIZE))

    for idx_rec in range(len(collide_recs)):
        rec = collide_recs[idx_rec]
        if rec_mouse.colliderect(rec):
            right_position = idx_positions[idx_rec]
            place_x = right_position[0]-1
            place_y = right_position[1]-1
            # pygame.draw.rect(WINDOW, COLOR_RED, rec)
            if place_x >= 0 and place_x < BOARD_SIZE and place_y >= 0 and place_y < BOARD_SIZE:
                if BOARD[place_x][place_y] == 0:
                    # print_move(place_x, place_y)
                    # break
                    return (BOARD_SIZE-place_x, LETTER[place_y])


def main():
    # opponent = AI_agent()
    run = True
    draw_window()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                # return "3,A"(board representation)
                PenteMove = get_pente_move(mouse_position)
                # place_stone: always get "3,A" as input, and place the stone in the board, so it returns the new board representation
                place_stone(True, PLAYER_COLOR, PenteMove)

                # TODO AI agent move
                # AI best move
                opponent_best_move, isWin = AI_best_move(BOARD, TIME_LEFT)
                PenteMove = (
                    BOARD_SIZE-opponent_best_move[0], LETTER[opponent_best_move[1]])
                place_stone(False, OPPONENT_COLOR, PenteMove)
                if isWin:
                    color_1 = (255, 153, 51)
                    color_2 = (107, 21, 219)
                    font = pygame.font.SysFont('georgia', 100)
                    text = font.render('AI beats you.',
                                       True, color_1, color_2)
                    textRect = text.get_rect()
                    textRect.center = (WIN_W // 2, WIN_H // 2)
                    WINDOW.blit(text, textRect)

            if event.type == pygame.MOUSEMOTION:
                # clock=pygame.time.Clock()
                # clock.get_time
                # mouse_position=pygame.mouse.get_focused()
                pass
                # mouse_position = pygame.mouse.get_pos()
                # place_stone(mouse_position)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
