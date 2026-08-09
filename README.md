# ⭕ Tic Tac Toe

A feature-rich, two-player CLI Tic Tac Toe game built with Python's Object-Oriented Programming principles.

## 🎯 Features 
**Core Gameplay**

- Two-Player Mode: Players take turns placing their signs on a 3x3 grid

- Multiple Sign Options: Choose from four different signs: ✅ ❎ ⭕ ❌

- Smart Turn Management: Random player selection for first move

- Win Detection: Checks all possible winning combinations (rows, columns, diagonals)

- Draw Detection: Identifies when the game ends in a draw

- Replay System: Play unlimited games in a single session

**Techical Highlights**

- Object-Oriented Design: Clear separation of concerns with three main classes

- Encapsulation: Proper use of private and public methods

- Error Handling: Comprehensive try-except blocks for all user inputs

- Modular Code: Well-organized project structure


## Project structure
```text
Tic Tac Toe/
├── Board/
│ └── board.py # Board class - manages the game grid
|
|
├── Player/
│ └── player.py # Player class - handles player data and sign selection
|
|
├── Game/
│ └── game.py # Game class - controls game logic and flow
|
|
├── .gitignore # Git ignore file
├── LICENSE # License file (MIT recommended)
└── README.md # Project documentation
```

## 🔧 Installation

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
python game.py
```

## 📋 Requirements
- Python 3.6+

## 🎮 How to play
**getting started**

1. Enter the first player's name

2. Enter the second player's name

3. First player selects their sign from: ✅ ❎ ⭕ ❌

4. Second player selects their sign (must be different)

5. The game randomly selects who plays first

**Game rules**

- Players take turns placing their signs on the board

- Use numbers 1-3 to specify row and column positions

- The first player to get 3 in a row (horizontal, vertical, or diagonal) wins

- If the board fills up with no winner, the game ends in a draw

**Controls**

- __Row Input__: Enter a number between 1-3

- __Column Input__: Enter a number between 1-3

- __Replay__: Type 'y' or 'n' when asked to play again

## Future improvements
- Implement AI opponent (single-player mode)
- Create a GUI version

## License
- MIT

## 👨‍💻 Author

- GitHub: @ZED-X3

## 📊 Project Status

- Status: ✅ Complete

- Last Updated: August 2026

- ⭐ Star this repository if you found it useful!