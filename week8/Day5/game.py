import random


AMOUNT_TO_WIN = 3


class Game:

    def __init__(self):
        self.user_item = ''
        self.computer_item = ''
        self.user_winning_round_counter = 0
        self.computer_winning_round_counter = 0
        self.round_results = {}
        self.user_winning_games = 0
        self.computer_winning_games = 0
        self.flag = True

    def get_user_item(self):
        items = ["r", "p", "s"]
        self.user_item = input("Select r(ock), p(aper), s(cissors)\n").lower()
        while self.user_item not in items:
            self.user_item = input("What do you play? (r | p | s)\n")
        return self.user_item

    def get_computer_item(self):
        items = ["r", "p", "s"]
        rand = random.Random()
        self.computer_item = rand.choice(items)
        return self.computer_item

    def new_round(self):
        self.show_round_results()
        result = self.get_round_results()
        if result == 'You won':
            self.user_winning_round_counter += 1
            print(f"{result} the round")
        elif result == 'You lost':
            self.computer_winning_round_counter += 1
            print(f"{result} the round")
        else:
            print(result)
        self.start_round()

    def get_round_results(self):
        if (self.user_item == 'r' and self.computer_item == 's') or \
                (self.user_item == 's' and self.computer_item == 'p') or \
                (self.user_item == 'p' and self.computer_item == 'r'):
            return "You won"
        if self.user_item == self.computer_item:
            return "A tie"
        return "You lost"

    def show_round_results(self):
        computer_item = self.get_computer_item()
        user_item = self.get_user_item()
        self.round_results['Player chose'] = user_item
        self.round_results['Computer chose'] = computer_item
        print('. '.join(f"{item}: {result}" for item, result in self.round_results.items()))

    def start_round(self):
        while self.user_winning_round_counter != AMOUNT_TO_WIN and self.computer_winning_round_counter != AMOUNT_TO_WIN:
            self.new_round()

    def show_game_results(self):
        while self.flag:
            if self.user_winning_round_counter == AMOUNT_TO_WIN or self.computer_winning_round_counter == AMOUNT_TO_WIN:
                if self.user_winning_round_counter == AMOUNT_TO_WIN:
                    winner = "Player"
                    self.user_winning_games += 1
                else:
                    winner = "computer"
                    self.computer_winning_games += 1
                print(f"The winner is the {winner}!\nGame results:\nYou won in {self.user_winning_round_counter} rounds\nThe computer won in {self.computer_winning_round_counter} rounds")
                self.flag = False

    def show_games_resume(self):
        print(f"Game resume: You won {self.user_winning_games} games, and the computer won {self.computer_winning_games} games")

    def show_menu(self):
        menu = input("Menu:\n(g) Play a new game\n(x)Show scores and exit\n").lower()
        if menu == "g":
            self.user_winning_round_counter = 0
            self.computer_winning_round_counter = 0
            self.start_round()
        elif menu == "x":
            self.show_game_results()
            self.show_games_resume()
            print("Thank you for playing!")


game = Game()
game.start_round()
game.show_menu()
