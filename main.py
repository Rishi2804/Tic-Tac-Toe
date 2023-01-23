import pygame, sys
 
pygame.init()

# Initialization Values
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
 
BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")
 
BG_COLOR = (255, 255, 255)
 
 # Board Setup
board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
 
turn = 'X'
 
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64, 64))
 
pygame.display.update()

#Functions

# Updates the board with the user placement
def render_board(board, ximg, oimg):
    global graphical_board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                # Create image and rect
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

# Upon click, add the visual for board placement
def add_XO(board, graphical_board, to_move):
    current_pos = pygame.mouse.get_pos()
    # offseted positions
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2
    # add only if spot is empty
    if board[round(converted_y)][round(converted_x)] == '_':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
    render_board(board, X_IMG, O_IMG)

    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
    
    return board, to_move


game_finished = False

def check_win(board):
    winner = None
    # check to see if player won via rows
    for row in range(len(board)):
        if (all(cell == board[row][0] for cell in board[row]) and board[row][0] != '_'):
            winner = board[row][0]
            for i in range(len(board)):
                graphical_board[row][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
            pygame.display.update()
            return winner
    # check to see if player won via coloumn
    for col in range(len(board[0])):
        if (all(row[col] == board[0][col] for row in board) and board[0][col] != '_'):
            winner = board[0][col]
            for i in range(len(board)):
                graphical_board[i][col][0] = pygame.image.load(f"assets/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
            pygame.display.update()
            return winner
    
    # Check to see if user won via diagonal
    if (all(board[i][i] == board[0][0] for i in range(len(board))) and board[0][0] != '_'):
        winner = board[0][0]
        for i in range(len(board)):
            graphical_board[i][i][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[i][i][0], graphical_board[i][i][1])
        pygame.display.update()
        return winner
    
    # Check to see if user won via diagonal
    if (all(board[i][len(board)-1-i] == board[0][len(board)-1] for i in range(len(board))) and board[0][len(board)-1] != '_'):
        winner = board[0][len(board)-1]
        for i in range(len(board)):
            graphical_board[i][len(board)-1-i][0] = pygame.image.load(f"assets/Winning {winner}.png")
            SCREEN.blit(graphical_board[i][len(board)-1-i][0], graphical_board[i][len(board)-1-i][1])
        pygame.display.update()
        return winner

    if winner is None:
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '_':
                    return None
        return "DRAW"

 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board, turn = add_XO(board, graphical_board, turn)

            if game_finished:
                board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
                graphical_board = [[[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]], 
                                    [[None, None], [None, None], [None, None]]]
                
                turn = 'X'
                
                SCREEN.fill(BG_COLOR)
                SCREEN.blit(BOARD, (64, 64))

                game_finished = False
                
                pygame.display.update()

            if check_win(board) is not None:
                game_finished = True
            
            pygame.display.update()