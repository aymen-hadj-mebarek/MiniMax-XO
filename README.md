# Tic-Tac-Toe Game with Minimax Algorithm

This project is a simple implementation of the classic Tic-Tac-Toe game in Python using the Pygame library. The game features an AI opponent that uses the Minimax algorithm to make optimal moves, ensuring that the AI will either win or force a draw if played perfectly.

## Project Overview

- **Player vs AI**: The player competes against an AI that uses the Minimax algorithm.
- **Restart Option**: The game includes a restart button to allow multiple rounds of play.

## Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used in two-player games like Tic-Tac-Toe. The algorithm simulates all possible moves, evaluates the outcomes, and chooses the best move to maximize the chance of winning (or minimize the chance of losing).

### How It Works:

1. **Maximizing Player (AI - 'O')**: The AI tries to maximize its score by choosing moves that lead to victory or at least a draw.
   
2. **Minimizing Player (Human - 'X')**: The human player is trying to minimize the AI's score by blocking its winning moves.

3. **Recursive Simulation**: The algorithm recursively explores all possible moves (until the game ends), assigning scores to game states:
   - Win: +1
   - Loss: -1
   - Draw: 0

4. **Backtracking**: After evaluating all possible outcomes, the algorithm backtracks to the current move, choosing the one with the best score for the AI.

## How to Run

### 1. Install the necessary libraries

Make sure you have Pygame installed. If not, you can install it using pip:

```bash
pip install pygame
```
### 2. Run the Game

Run the Python script to start the game:

```bash
python tic_tac_toe.py
```
## Game Rules

- The game is played on a 3x3 grid.
- The player ('X') and the AI ('O') take turns to mark empty squares.
- The first to align three of their marks vertically, horizontally, or diagonally wins.
- If all squares are filled without a winner, the game ends in a draw.

## Project Structure

- `tic_tac_toe.py`: The main Python file containing the game logic, including the Minimax algorithm.
- The Pygame window displays the game board, current player's turn, and the result of the game.

## Features

- **Minimax AI**: Ensures optimal play by the AI, making it unbeatable if played correctly.
- **User Interface**: A simple graphical interface built with Pygame, including a restart button.
- **Player vs AI**: The player plays as 'X', and the AI plays as 'O'.

## Understanding the Code

- **Class `square`**: Represents each square on the Tic-Tac-Toe grid. It handles drawing the square, detecting player clicks, and updating its state.
    
- **Class `button`**: Represents the restart button to reset the game.
    
- **Function `minimax`**: Implements the Minimax algorithm to evaluate the best move for the AI.
    
- **Function `check_win`**: Checks for a win or draw condition in the game.
    

## Notes

- This project demonstrates the application of the Minimax algorithm in a simple game setting, providing a foundation for understanding AI in games.
- The project is designed for educational purposes, particularly for those interested in game development and AI algorithms.

## Future Improvements

- Adding difficulty levels by limiting the depth of the Minimax search.
- Enhancing the user interface with more interactive features and better graphics.
- Implementing multiplayer mode or additional AI strategies.