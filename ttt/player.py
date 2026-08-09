class Player:
    def __init__(self):
        self.player_name = None
        self.sign = None

    def enter_name(self, message):
        while True:
            try:
                self.player_name = input(message)

                if not self.player_name.strip():
                    raise ValueError

                return self.player_name

            except ValueError:
                print('name can not be empty!')

    def enter_sign(self, message):

        while True:
            try:
                valid_signs = ['✅', '❎', '⭕', '❌']
                print(f"choose: {'  '.join(valid_signs)}")

                self.sign = input(message)

                if self.sign not in valid_signs:
                    raise ValueError

                return self.sign

            except ValueError:
                print('the sign must be among the vaild ones!')

    def __str__(self):
        return self.player_name
