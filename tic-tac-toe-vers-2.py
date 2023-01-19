
players = None
def greet():
    global players
    print(" Привет! \n Это * Игра Крестики-нолики * \n Цель игры поставить три одинаковых символа в ряд или по диагонали \n Для того чтобы поставить символ просто введи номер поля, куда хотел бы поставить символ \n Играя с компьютером он ходит первым\n Для начала укажи , количество игроков? \n 1 - если хочешь сыграть с компьютером \n 2 - если играешь с другом" )
    while True:
        players = input()
        if not (players.isdigit()):
            print(" Введите числа! ")
          #  print(players, "1")
            continue
        if int(players) == 1:
            return players
          #  print(players, "2")
        elif int(players) == 2:
            return players
           # print(players, "3")
        else:
            print("Некорректное значение \nВведи: \n 1 - если хочешь сыграть с компьютером \n 2 - если играешь с другом")
          #  print(players, "4")
            continue
import random
def rand_game():
    while True:
        pc = random.randint(1, 9)
        #player_answer = pc
        if (str(board[pc - 1]) not in "XO"):
            board[pc - 1] = "X"
            print("Ход компьютера")
        return pc
board = list(range(1,10))
def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)
count = 0
def take_input(player_token):
      while True:
       if int(players) == 2:
            player_answer = input("Куда поставим " + player_token+"? ")
            if not (player_answer.isdigit()):
                print(" Введите номер клетки! ")
                #  print(players, "1")
                continue
            player_answer = int(player_answer)
            if player_answer >= 1 and player_answer <= 9:
                if(str(board[player_answer-1]) not in "XO"):
                    board[player_answer-1] = player_token
                    break
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
       else:
            continue
def take_input_pc(player_token):
       if int(players) == 1:
            while True:
                rand_game()
                player_answer = input("Куда поставим " + player_token+"? ")
                if not (player_answer.isdigit()):
                    print(" Введите номер клетки!! ")
                    #  print(players, "1")
                    continue
                player_answer = int(player_answer)
                if player_answer >= 1 and player_answer <= 9:
                    if (str(board[player_answer - 1]) not in "XO"):
                        board[player_answer - 1] = player_token
                        break
                    else:
                        print("Эта клетка уже занята!")
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False
def main(board):
    if int(players) == 2:
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
               take_input("X")
            else:
               take_input("O")
            counter += 1
            if counter > 4:
               tmp = check_win(board)
               if tmp:
                  print(tmp, "выиграл!")
                  win = True
                  break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)
    elif int(players) == 1:
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                rand_game()
                #take_input_pc("X")
            else:
                take_input_pc("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        draw_board(board)
greet()
main(board)
input("Нажмите Enter для выхода!")