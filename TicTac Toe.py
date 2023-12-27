import os

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" %s  | %s | %s | " % (self.cells[1], self.cells[2], self.cells[3]))
        print(" ---------------")
        print(" %s  | %s | %s | " % (self.cells[4], self.cells[5], self.cells[6]))
        print(" ---------------")
        print(" %s  | %s | %s | " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player


def print_header():
    print("Welcome To Tic-Tac-Toe\n")


def refresh_screen():
    # Clear the screen
    os.system("clear")


def get_player_choice(player):
    while True:
        try:
            choice = int(input(f"\n{player}) Please choose 1 - 9. >"))
            if 1 <= choice <= 9 and board.cells[choice] == " ":
                return choice
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


board = Board()
print_header()

while True:
    refresh_screen()

    # Identify X input and Get X input
    x_choice = get_player_choice("X")

    # Update board
    board.update_cell(x_choice, "X")

    # Show the updated board
    board.display()

    # Refresh O board
    refresh_screen()

    # Identify O input and Get O input
    o_choice = get_player_choice("O")

    # Update board
    board.update_cell(o_choice, "O")
  