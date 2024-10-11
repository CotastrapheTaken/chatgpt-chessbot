# chatgpt-chessbot

only sharing this here cuz my friends wants to see the code



### chatgpt'd readme

# Chess Bot with AI

## Overview

This project implements a simple chess bot using Python and the Pygame library. The bot utilizes the Stockfish chess engine to make moves. It features a graphical user interface (GUI) where you can see the chess pieces on the board and control the flow of the game with a "Next Move" button.

## Features

- Visual representation of a chess board with pieces
- Ability to make moves using the Stockfish chess engine
- Manual control to advance to the next move by clicking a button

## Requirements

- Python 3.x
- Pygame library
- Chess library
- Chess-engine library
- Stockfish chess engine

## Installation

1. **Install Python**: Make sure you have Python 3.x installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Install the required libraries using pip:
   ```bash
   pip install pygame chess chess-engine

Download Stockfish: Download the Stockfish chess engine from [stockfishchess.org](https://stockfishchess.org/). Extract the files and note the path to the stockfish executable.

Chess Pieces Images: Place the chess piece images in a folder named pieces within the project directory. Ensure the images follow this naming convention:

- b-bishop.png
- b-king.png
- b-knight.png
- b-pawn.png
- b-queen.png
- b-rook.png
- w-bishop.png
- w-king.png
- w-knight.png
- w-pawn.png
- w-queen.png
- w-rook.png

Update the Code: In the code, make sure to set the correct path to the Stockfish executable and the images. For example:
```bash 
engine = chess.engine.SimpleEngine.popen_uci(r"your_path_to_stockfish_executable")
```

## Code Explanation

The code initializes a Pygame window, creates a chess board with a 100x100 pixel tile size, loads the images for the chess pieces, and allows for basic interaction to see the AI make moves. The main functionalities include:

1. Pygame Initialization: Setting up the Pygame library and creating the main window.
2. Loading Images: Loading chess piece images based on a naming convention.
3. Drawing the Board: Rendering the chess board and pieces on the screen.
4. AI Move Logic: Using the Stockfish engine to determine the next move and update the board accordingly.
5. Next Move Button: A button to allow users to advance the game and see the AI's next move.
6. Run the script using Python:
```bash
python chess_bot.py
```
A window will open displaying the chess board. Click the "Next Move" button to make the AI take its turn.

### Contributing
Feel free to fork the repository, make improvements, or submit pull requests. Any contributions are welcome!

### License
This project is open source and available under the MIT License.

> [!IMPORTANT]
> THIS IS NOT MY CODE, THIS IS ALL PURE CHATGPT, MY FRIEND WANTS TO SEE THE CODE.


> [!IMPORTANT]
> **THIS CODE IS MAINLY CHATGPT, I HAD ALMOST NO INPUT, THIS IS NOT MY WORK**

