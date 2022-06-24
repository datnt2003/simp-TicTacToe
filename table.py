def check_input_opt(num):
    if num < 1 or num > 9:
        return False
    else:
        return True


def nhap():
    while True:
        num = int(input())
        if check_input_opt(num):
            return num


def kiem_tra_ton_tai(num, table):
    for i in range(len(table)):
        for j in range(len(table)):
            if num == table[i][j]:
                return True
    return False


def emt(Player, opt, table):
    for i in range(len(table)):
        for j in range(len(table)):
            if opt == table[i][j]:
                table[i][j] = Player.get_sym()

def full_table(dem,table):
    for row in table:
        for col in row:
            if type(col) == str:
                dem -= 1
    if dem == 0:
        return True
    else:
        return False


class Table(object):
    def __init__(self):
        self.opt = None
        self.table = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

    def get_table(self):
        return self.table

    def show_table(self):
        for row in self.table:
            for col in row:
                print("{}".format("-"),end=" ") if type(col)==int else print("{}".format(col),end=" ")
            print()

    def fill(self, Player):
        self.opt = int(input())
        if not kiem_tra_ton_tai(self.opt, self.table):
            self.opt = nhap()
            emt(Player, self.opt, self.table)
        else:
            emt(Player, self.opt, self.table)

    def check_win(self, Player):
        # row
        if self.table[0][0] == Player.get_sym() and self.table[1][0] == Player.get_sym() and self.table[2][
            0] == Player.get_sym():
            return True
        elif self.table[1][0] == Player.get_sym() and self.table[1][1] == Player.get_sym() and self.table[1][
            2] == Player.get_sym():
            return True
        elif self.table[2][0] == Player.get_sym() and self.table[2][1] == Player.get_sym() and self.table[2][
            2] == Player.get_sym():
            return True
        # col
        elif self.table[0][0] == Player.get_sym() and self.table[0][1] == Player.get_sym() and self.table[0][
            2] == Player.get_sym():
            return True
        elif self.table[1][0] == Player.get_sym() and self.table[1][1] == Player.get_sym() and self.table[1][
            2] == Player.get_sym():
            return True
        elif self.table[2][0] == Player.get_sym() and self.table[2][1] == Player.get_sym() and self.table[2][
            2] == Player.get_sym():
            return True
        # dc
        elif self.table[0][0] == Player.get_sym() and self.table[1][1] == Player.get_sym() and self.table[2][
            2] == Player.get_sym():
            return True
        elif self.table[0][2] == Player.get_sym() and self.table[1][1] == Player.get_sym() and self.table[2][
            0] == Player.get_sym():
            return True
        else:
            return False

    def reset_table(self):
        self.table = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
