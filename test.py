
name_player_1 = ""
name_player_2 = ""


def name_player():  # додавання ім'я ігрока
    global  name_player_1
    name_player_1 = input("Enter name player 1: ")
    name_player_2 = input("Enter name player 2: ")
    return name_player_1
def visual_game(param_1):
    print('(*-*)=(*-*)'*5)
    print(f'Player 1:                                      Player 2:')
    print(param_1)


name_player()
print(name_player_1)
visual_game(name_player_1)