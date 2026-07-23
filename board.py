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

        changed_rows = "\n----------\n".join(rows)

        return changed_rows
    
    def reset_board(self):
        return self.board
