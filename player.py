class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.sign = None

    def enter_sign(self):
        self.sign = input('choose from the signs:')
        return self.sign

    def choose_sign(self):
        valid_signs = "  ".join(['✅', '❎', '⭕', '❌'])

        print(valid_signs)
        self.enter_sign()

        while self.sign not in valid_signs:

            print(f'please choose the right sign.')
            self.enter_sign()

        return f"{self.player_name}'s chosen sign is: {self.sign}"
