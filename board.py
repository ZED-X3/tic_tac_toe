class Board:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    
    def show_board(self):
        rows = []

        for row in self.board:
            row = ' | '.join(row)
            rows.append(row)

        display_board = "\n----------\n".join(rows)

        return display_board
    
    def reset_board(self):
        for row in range(3):
            for column in range(3):
                self.board[row][column] = " "

        return self.board

    def get_cell(self, row, column):
        return self.board[row][column]

    def place_sign(self, row, column, sign):
        self.board[row][column] = sign
