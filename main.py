import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

symbol_counts = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines

def get_slot_machine_spin(rows, columns, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns_list = []
    for _ in range(columns):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns_list.append(column)

    return columns_list

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(f"{column[row]} |", end=" ")
            else:
                print(column[row])

def deposit():
    return get_valid_input(
        "Enter the amount you want to deposit: $",
        "Enter a number greater than 0.",
        lambda x: x > 0
    )

def get_number_of_lines():
    return get_valid_input(
        f"Enter the number of lines to bet on (1-{MAX_LINES}): ",
        f"Enter a number between 1 and {MAX_LINES}.",
        lambda x: 1 <= x <= MAX_LINES
    )

def get_bet():
    return get_valid_input(
        f"Enter the amount you want to bet on each line ({MIN_BET}-{MAX_BET}): $",
        f"Enter an amount between {MIN_BET} and {MAX_BET}.",
        lambda x: MIN_BET <= x <= MAX_BET
    )

def get_valid_input(prompt, error_msg, condition_func):
    while True:
        user_input = input(prompt).strip()
        
        if user_input.isdigit():
            user_input = int(user_input)
            if condition_func(user_input):
                return user_input
            else:
                print(error_msg)
        else:
            print("Enter a positive number.")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines and your total bet is ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_counts)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: ", *winning_lines)
    else:
        print("You didn't win on any lines.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

if __name__ == "__main__":
    main()
