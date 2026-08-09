from board import Board
from player import Player
import random

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

        self.board = Board()

        self.current_player = None

        self.player1_sign = None
        self.player2_sign = None

    def choose_sign(self):
        self.player1_sign = self.player1.enter_sign('enter first player\'s sign: ')

        while True:
            try:
                self.player2_sign = self.player2.enter_sign('enter second player\'s sign: ')

                if self.player1_sign == self.player2_sign:
                    raise ValueError

                return self.player1_sign, self.player2_sign

            except ValueError:
                print('signs can not be chosen the same!')

    def plays_first(self):
        player_list = [self.player1, self.player2]
        first_player = random.choice(player_list)

        return first_player

    def start_game(self):

            self.player1.enter_name('enter first player\'s name: ')
            self.player2.enter_name('enter second player\'s name: ')

            self.current_player = self.plays_first()
    
            return self.current_player, self.choose_sign()

    def get_number(self, message):
        while True:
            try:
                number = int(input(message))

                if number not in [1, 2, 3]:
                    raise ValueError

                return number

            except ValueError:
                print('the entered number is not valid!')
    
    def player_move(self):
        sign = self.current_player.sign

        while True:
            row = self.get_number('enter which row: ') - 1
            column = self.get_number('enter which column: ') - 1

            if self.board.is_empty(row, column):
                self.board.place_sign(row, column, sign)
                self.switch_turn()
                return True

            print('the selected section is not empty.')

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        return self.current_player

    def winning_status(self):

        board = self.board.get_board()

        main_diag = [board[i][i] for i in range(3)]
        if all(win == self.player1_sign for win in main_diag):
            return(f'{self.player1.player_name} won.')

        elif all(win == self.player2_sign for win in main_diag):
            return(f'{self.player2.player_name} won.')

        sub_diag = [board[i][3 - i - 1] for i in range(3)]
        if all(win == self.player1_sign for win in sub_diag):
            return(f'{self.player1.player_name} won.')

        elif all(win == self.player2_sign for win in sub_diag):
            return(f'{self.player2.player_name} won.')

        for n in range(0,3):
            columns = [board[i][n] for i in range(3)]
            if all(win == self.player1_sign for win in columns):
                return(f'{self.player1.player_name} won.')

            elif all(win == self.player2_sign for win in columns):
                return(f'{self.player2.player_name} won.')

            rows = [board[n][i] for i in range(3)]
            if all(win == self.player1_sign for win in rows):
                return(f'{self.player1.player_name} won.')
            
            elif all(win == self.player2_sign for win in rows):
                return(f'{self.player2.player_name} won.')

        return False

    def is_draw(self):

        board = self.board.get_board()

        for row in board:
            if " " in row:
                return False

        return True

    def run_game(self):
        self.start_game()

        print(self.board.show_board())

        while True:

            print(f'{self.current_player}\'s turn')
            self.player_move()
            print(self.board.show_board())

            winner = self.winning_status()

            if winner:
                print(winner)
                break

            if self.is_draw():
                print('the game has ended with a draw result')
                break

    def game_flag(self):

        while True:
            try:
                self.flag = input('do you want to play?:' )

                if self.flag not in ['y', 'Y', 'n', 'N']:
                    raise ValueError

                return self.flag

            except ValueError:
                print('choose a valid choice!')

    def new_game(self):
        
        while self.game_flag() in ['y', 'Y']:
            self.board.reset_board()
            self.run_game()

        return f'the game has ended.'


if __name__ == "__main__":
    print("=" * 50)
    print("🎮 TIC-TAC-TOE GAME TEST 🎮")
    print("=" * 50)

    game = Game()
    game.new_game()
