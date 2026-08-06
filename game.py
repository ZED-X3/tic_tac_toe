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

        board = self.board.get_board()

        main_diag = [board[i][i] for i in range(3)]
        if all(win == self.player1.sign for win in main_diag):
            return(f'{self.player1.player_name} won.')

        elif all(win == self.player2.player_name.sign for win in main_diag):
            return(f'{self.player2.player_name} won.')

        sub_diag = [board[i][3 - i - 1] for i in range(3)]
        if all(win == self.player1.player_name.sign for win in sub_diag):
            return(f'{self.player1.player_name} won.')

        elif all(win == self.player2.player_name.sign for win in sub_diag):
            return(f'{self.player2.player_name} won.')

        for n in range(0,3):
            columns = [board[i][n] for i in range(3)]
            if all(win == self.player1.player_name.sign for win in columns):
                return(f'{self.player1.player_name} won.')

            elif all(win == self.player2.player_name.sign for win in columns):
                return(f'{self.player2.player_name} won.')

            rows = [board[n][i] for i in range(3)]
            if all(win == self.player1.player_name.sign for win in rows):
                return(f'{self.player1.player_name} won.')
            
            elif all(win == self.player2.player_name.sign for win in rows):
                return(f'{self.player2.player_name} won.')

        return False

    def run_game(self):
        self.start_game()

        if not self.winning_status():
            self.player_move()
        else:
            self.board.reset_board()

    def game_flag(self):
        self.flag = input('do you want to play?:' )
        return self.flag

    def new_game(self):
        self.game_flag()
        while self.flag == 'y':
            self.run_game()
            self.game_flag()
        else:
            return f'the game has ended.'