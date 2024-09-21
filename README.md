# Slot Machine Game 🎰

A simple command-line slot machine game implemented in Python. Players can deposit funds, place bets on multiple lines, and spin the slot machine to win or lose money based on randomized outcomes.

## 📝 Features

- **Deposit Funds**: Start by depositing an initial balance.
- **Bet on Lines**: Bet on up to 3 lines for each spin.
- **Flexible Betting**: Choose your bet amount per line (within limits).
- **Randomized Spins**: Each spin results in a random set of symbols.
- **Payouts**: Winnings are calculated based on matching symbols and their assigned values.
- **Track Balance**: Keep track of your current balance as you play.

## 🎮 How to Play

1. **Deposit Money**: Enter an amount to deposit and start playing.
2. **Choose Lines**: Select how many lines you want to bet on (1 to 3).
3. **Place a Bet**: Set the amount you want to bet per line.
4. **Spin the Slot Machine**: Random symbols will appear in the 3x3 grid. If matching symbols appear on your chosen lines, you win!
5. **Winnings**: Winnings are calculated based on the symbol values and the amount you bet.

## 🎰 Symbol Values

Each symbol has a different payout value and appears in different quantities on the slot machine:

| Symbol | Count | Value (Multiplier) |
|--------|-------|--------------------|
|   A    |   2   |        5x          |
|   B    |   4   |        4x          |
|   C    |   6   |        3x          |
|   D    |   8   |        2x          |

The more rare the symbol, the higher the payout! You win by matching symbols across the columns in the selected lines.

## 🔧 Code Overview

- `check_winnings()`: Checks if the symbols on the betted lines match and calculates the winnings.
- `get_slot_machine_spin()`: Randomly generates the slot machine spin based on the symbol counts.
- `print_slot_machine()`: Displays the current slot machine spin in a grid format.
- `deposit()`: Prompts the player to deposit an initial balance.
- `get_number_of_lines()`: Allows the player to choose the number of lines to bet on.
- `get_bet()`: Retrieves the player's bet per line and ensures it is within the allowed range.
- `spin()`: Executes the main game round, calculates winnings, and updates the player's balance.
- `main()`: The main loop to manage multiple game rounds and check if the player wants to continue or quit.

## ⚙️ Requirements

- Python 3.x

## 📄 License

This project is licensed under the MIT License.

