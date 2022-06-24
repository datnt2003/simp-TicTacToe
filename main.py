import os

import table
from table import Table
from player import Player
import random

clear = lambda: os.system('cls')

turn = random.randint(0, 1)

tb = Table()
player_sym = ["x", "o"]
p1 = Player(player_sym[0])
p2 = Player(player_sym[1])
while True:
    dem = 9
    tb.show_table()
    if turn % 2 == 0:
        print(f"{player_sym[0]}")
        tb.fill(p1)
        tb.show_table()
        if tb.check_win(p1) and table.full_table(dem, tb.get_table()) == False:
            # clear()
            print("x-won")
            print("choi lai ?")
            if input() == "y":
                tb.reset_table()
            else:
                exit()
    elif turn % 2 != 0:
        print(f"{player_sym[1]}")
        tb.fill(p2)
        tb.show_table()
        if tb.check_win(p2) and table.full_table(dem, tb.get_table()) == False:
            # clear()
            print("o-won")
            print("choi lai ?")
            if input() == "y":
                tb.reset_table()
            else:
                exit()

    if table.full_table(dem, tb.get_table()):
        print("o-x")
        print("choi lai ?")
        if input() == "y":
            tb.reset_table()
        else:
            exit()
    turn += 1
    clear()
