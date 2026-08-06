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

    # def get_cell(self, row, column):
    #     return self.board[row][column]

    def place_sign(self, row, column, sign):
        if self.is_empty(row, column):
            self.board[row][column] = sign
        else:
            return f'the selected section is not empty.'

    def get_board(self):
        return self.board

    def is_empty(self, i, j):
        return self.board[i][j] == " "   