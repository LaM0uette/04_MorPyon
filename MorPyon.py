import os
import time
from enum import Enum
from termcolor import colored


class Player(Enum):
    Player1 = 1
    Player2 = 2


class NewGame:
    def __init__(self):
        self.run = True
        self.size_game = 3
        self.player_turn = Player.Player1
        self.matrix_game = self.gen_matrice()
        self.matrix_win = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 2], [1, 1], [0, 0]],
        ]

    def gen_matrice(self):
        lst = []

        for row in range(self.size_game):
            lst.append([])

            for _ in range(self.size_game):
                lst[row].append(0)

        return lst

    def init_display(self):
        os.system(f"mode con: cols={38+(self.size_game**2)} lines={4+self.size_game}")

    def draw_game(self):
        os.system("cls")

        print(f"Tour: {self.player_turn.name}" if self.run else '')

        for i in range(self.size_game):
            print(f"""                   {''.join(f"[{colored('O', 'yellow') if x == 1 else colored('X', 'red') if x == 2 else colored('O', 'green', attrs=['bold']) if x == 3 else colored('X', 'green', attrs=['bold']) if x == 6 else ' '}]" for x in self.matrix_game[i])}""")

        print("")
        
    def player_play(self, num_played):
        if not num_played.isdigit() or not 0 < int(num_played) < self.size_game**2 + 1:
            print("Valeur incorect !")
            time.sleep(0.5)
            return

        num = int(num_played) - 1

        if 0 <= num <= 2:
            col = num
            row = 2
        elif 3 <= num <= 5:
            col = num - 3
            row = 1
        else:
            col = num - 6
            row = 0

        if self.matrix_game[row][col] == 0:
            self.matrix_game[row][col] = self.player_turn.value
        else:
            print("Impossible de jouer ici !")
            time.sleep(1)
            return

        self.check_win()
        self.check_end()

        self.player_turn = Player.Player2 if self.player_turn == Player.Player1 else Player.Player1

    def check_win(self):
        for matrix in self.matrix_win:
            for i in matrix:
                if self.matrix_game[i[0]][i[1]] != self.player_turn.value:
                    return

        self.end_game(f"{self.player_turn.name} à gagné la partie !")


    def check_end(self):
        for item in self.matrix_game:
            if 0 in item:
                return

        self.end_game("Grille pleine !")

    def end_game(self, msg):
        self.run = False
        self.draw_game()
        print(f"{colored(msg, 'yellow') if self.player_turn.value == 1 else colored(msg, 'red')}")

    def start(self):
        self.init_display()

        while self.run:
            self.draw_game()

            input_player = input(f"Entrez le numéro d'une case (1 - {self.size_game**2}) : ")
            self.player_play(num_played=input_player)

NewGame().start()