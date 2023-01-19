status_players = None

def greet():
    global status_players
    print(" ----------------------------------")
    print("           Приветсвуем вас  ")
    print("               в игре       ")
    print("           крестики-нолики  ")
    print(" ----------------------------------")
    print(" Если играете с другом введите duo ")
    print(" ----------------------------------")
    print(" Если играете в соло введите символ")
    print(" которым хотите играть, |x| или |o|")
    while True:
        status_players = str(input())
        if status_players == "x" or status_players == "o" or status_players == "duo":
            return status_players
            print(" ----------------------------------")
            print("        формат ввода: x y         ")
            print("        x - номер строки          ")
            print("        y - номер столбца         ")
            break
        else:
            print("Введите одно из трех значений \n duo /  x  /  o  ")
            continue

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

import random

def rand_game():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if field[x][y] != " ":
            continue
        return x, y

def ask():
    while True:
        cords = input("         Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if status_players == "duo":
            if symbols == ["x", "x", "x"]:
                print("Выиграл X!!!")
                print("   Спасибо за игру!   ")
                return True
            if symbols == ["o", "o", "o"]:
                print("Выиграл o!!!")
                print("   Спасибо за игру!   ")
                return True
        elif status_players == "x":
            if symbols == ["x", "x", "x"]:
                print("Вы выиграли!!!")
                print("   Спасибо за игру!   ")
                return True
            if symbols == ["o", "o", "o"]:
                print("Вы проиграли!!!")
                print("   Спасибо за игру!   ")
                return True
        else:
            if symbols == ["x", "x", "x"]:
                print("Вы проиграли!!!")
                print("   Спасибо за игру!   ")
                return True
            if symbols == ["o", "o", "o"]:
                print("Вы выиграли!!!")
                print("   Спасибо за игру!   ")
                return True
    return False


greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if status_players == "duo":
        if count % 2 == 1:
            print(" Ходит крестик!")
        else:
            print(" Ходит нолик!")

        x, y = ask()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            break
    elif status_players == "x":
        if count % 2 == 1:
            print(" Ходите!")
            x, y = ask()
            field[x][y] = "x"
        else:
            print(" Ход компьютера!")
            x, y = rand_game()
            field[x][y] = "o"

        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            break
    elif status_players == "o":
        if count % 2 == 1:
            print(" Ход компьютера!")
            x, y = rand_game()
            field[x][y] = "x"
        else:
            print(" Ходите!")
            x, y = ask()
            field[x][y] = "o"

        if check_win():
            break

        if count == 9:
            print(" Ничья!")
            break
    else:
        print ("Введите duo, x или o")


