import os
import time
from enum import Enum
from termcolor import colored

SIZE_GAME = 3


class Player(Enum):
    Player1 = 1
    Player2 = 2


class NewGame:
    def __init__(self):
        self.run = True
        self.player_turn = Player.Player1
        self.matrix_game = self.gen_matrice()

    def gen_matrice(self):
        lst = []

        for row in range(SIZE_GAME):
            lst.append([])

            for col in range(SIZE_GAME):
                lst[row].append(0)

        return lst

    def draw_game(self):
        os.system("cls")

        print(f"Tour: {self.player_turn.name}" if self.run else '')

        for i in range(SIZE_GAME):
            print(f"""                   {''.join(f"[{colored('O', 'yellow') if x == 1 else colored('X', 'red') if x == 2 else colored('O', 'green', attrs=['bold']) if x == 3 else colored('X', 'green', attrs=['bold']) if x == 6 else ' '}]" for x in self.matrix_game[i])}""")

        print("")

    def start(self):
        os.system(f"mode con: cols={38} lines={7}")

        while self.run:
            self.draw_game()

            input_player = input(f"Entrez le numéro d'une colonne (1 - {SIZE_GAME**2}) : ")
            # self.add_token(token_played=input_player)

NewGame().start()