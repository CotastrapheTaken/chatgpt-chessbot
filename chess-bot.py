import pygame
import chess
import chess.engine
import os

# Initialize pygame
pygame.init()

# Board setup
SQUARE_SIZE = 100  # Each square is 100x100 pixels
WIDTH, HEIGHT = SQUARE_SIZE * 8, SQUARE_SIZE * 8 + 50  # Added height for the "Next" button
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (50, 205, 50)  # Green for button
BUTTON_TEXT_COLOR = (255, 255, 255)  # White text

# Load the chess pieces using relative paths
pieces_images = {}
pieces_folder = os.path.join("pieces")  # Folder containing piece images
for piece in ['b-bishop', 'b-king', 'b-knight', 'b-pawn', 'b-queen', 'b-rook', 
              'w-bishop', 'w-king', 'w-knight', 'w-pawn', 'w-queen', 'w-rook']:
    pieces_images[piece] = pygame.transform.scale(pygame.image.load(
        os.path.join(pieces_folder, f"{piece}.png")), (SQUARE_SIZE, SQUARE_SIZE))

# Create the display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Bot")

# Function to draw the board
def draw_board():
    colors = [WHITE, BLACK]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw pieces on the board
def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                color = 'w' if piece.color == chess.WHITE else 'b'
                piece_type = piece.piece_type
                piece_symbol = {chess.KING: 'king', chess.QUEEN: 'queen', chess.ROOK: 'rook',
                                chess.BISHOP: 'bishop', chess.KNIGHT: 'knight', chess.PAWN: 'pawn'}
                piece_image = pieces_images[f"{color}-{piece_symbol[piece_type]}"]
                screen.blit(piece_image, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw the "Next" button
def draw_next_button():
    button_rect = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Next Move", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

# Function to update the board with moves
def update_board(board):
    draw_board()
    draw_pieces(board)
    draw_next_button()
    pygame.display.flip()  # Update the display after drawing everything

# Chess engine setup (using Stockfish)
stockfish_path = os.path.join("stockfish", "stockfish-windows-x86-64-avx2.exe")  # Path to the Stockfish executable
engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
board = chess.Board()

# Main loop
running = True
waiting_for_next_move = False  # Wait until button is pressed
while running:
    update_board(board)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if HEIGHT - 50 <= mouse_pos[1] <= HEIGHT:
                waiting_for_next_move = True  # If the button is clicked

    if waiting_for_next_move and not board.is_game_over():
        if board.turn:  # white (AI)
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)
        else:  # black (AI)
            result = engine.play(board, chess.engine.Limit(time=0.1))
            board.push(result.move)

        waiting_for_next_move = False  # Reset until next button press

# Quit chess engine and pygame
engine.quit()
pygame.quit()
