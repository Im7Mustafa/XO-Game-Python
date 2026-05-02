# XO Game in Python 🎮

Hi everyone! This is Mustafa. I built this interactive XO (Tic-Tac-Toe) game completely from scratch using Python. I took this project as a personal challenge to write clean, modular code and apply core programming logic without relying on any external libraries.

## 💡 How I Built It
I structured the code to be as readable and efficient as possible by breaking the game down into core concepts:

* **2D Lists (Matrices):** I used a 3x3 list to represent the game board, making it easy to track positions from 1 to 9.
* **Modular Functions:** The game relies on specific functions handling single tasks:
  * `showGame()`: Prints the board to the console.
  * `playRule()`: Handles player input and uses a `while True` loop to ensure valid moves (preventing players from overwriting an already taken spot!).
  * `changeRule()`: Simply swaps the turns between 'X' and 'O'.
  * `checkWin()`: Uses chained comparisons to check all rows, columns, and diagonals for a winner.
* **The Main Engine:** A continuous `while` loop that brings everything together, counts the moves (capping at 9 to detect a tie), and manages the game flow.

## 🚀 How to Play
1. Download the Python file.
2. Run it in your terminal/command prompt:
   ```bash
   python XO.py
