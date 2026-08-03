from board import Board
from player import Player
import random

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

        self.board = Board()
        self.current_player = None

    def plays_first(self):
        player_list = [self.player1, self.player2]
        first_player = random.choice(player_list)

        return first_player

    def start_game(self):
            self.current_player = self.plays_first()
    
            return self.current_player
    
    def player_move(self):
        sign = self.current_player.sign

        row = int(input('enter row:'))
        column = int(input('enter column:'))

        self.board.place_sign(row, column, sign)

        self.switch_turn()

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return self.current_player

    def winning_status(self):

        board = self.board.get_cell()

        main_diag = [board[i][i] for i in range(3)]
        if all(win == self.player1.sign for win in main_diag):
            print(f'{self.player1} won.')

        elif all(win == self.player2.sign for win in main_diag):
            print(f'{self.player2} won.')

        sub_diag = [board[i][3 - i - 1] for i in range(3)]
        if all(win == self.player1.sign for win in sub_diag):
            print(f'{self.player1} won.')

        elif all(win == self.player2.sign for win in sub_diag):
            print(f'{self.player2} won.')

        for n in range(0,3):
            columns = [board[i][n] for i in range(3)]
            if all(win == self.player1.sign for win in columns):
                print(f'{self.player1} won.')

            elif all(win == self.player2.sign for win in columns):
                print(f'{self.player2} won.')

            rows = [board[n][i] for i in range(3)]
            if all(win == self.player1.sign for win in rows):
                print(f'{self.player1} won.')
            
            elif all(win == self.player2.sign for win in rows):
                print(f'{self.player2} won.')
