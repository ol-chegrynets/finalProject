"""import random
import deck_of_cards


desc_player_1 = []      # колода гравця 1
desc_player_2 = []      # колода гравця 2
#cards_player_1 = 0      # карта на роздачі гравця 1
#cards_player_2 = 0      # карта на роздачі гравця 2

desk_of_cards = []      # list із карт, перемішаний

name_player_1 = "str"
name_player_2 = "str"


def name_player():      #  додавання ім'я ігрока
    name_player_1 = input("Enter name player 1: ")
    name_player_2 = input("Enter name player 2: ")

def exit_game():     # преривання гри на вимогу, наприклад клав."esc"
    pass



# def visual_distrib():        # вызуальне роздавання карт на двох.
#    pass


def distribution_of_cards(cards):      # розділ колоди на 2 частини
    for i in cards:
         if random.randint(0, 1):
             desc_player_1.append(i)
         else:
             desc_player_2.append(i)

    while len(desc_player_1) != len(desc_player_2):
        if len(desc_player_1) < len(desc_player_2):
            x = random.randint(0, len(desc_player_2))
            a = desc_player_2.pop(x)
            desc_player_1.append(a)
        else:
            x = random.randint(0, len(desc_player_1))
            a = desc_player_1.pop(x)
            desc_player_2.append(a)

    print(len(desc_player_1), desc_player_1)
    print(len(desc_player_2), desc_player_2)
    return desc_player_1, desc_player_2

def put_card():     # покласти карту на роздчу
    #print("Press the letter l  ")       #  розмістити в верхньлму провому куті
    #print("Press the letter s  ")       #  розмістити в верхньлму лівому куті
    x = 0
    y = 0
    while (x < 1 or y < 1):         #  натисни кнопку - selection_card() - карта лягла на стіл
        if x == 0: print("Press the letter s  ")
        if y == 0: print("Press the letter L  ")
        pres_button = input()
        if pres_button == "s":
            cards_player_1 = selection_card(desc_player_1)
            print(cards_player_1)
            x = 1
            continue
        elif  pres_button == "l":
                cards_player_2 = selection_card(desc_player_2)
                print(cards_player_2)
                y = 1
                continue

    return cards_player_1, cards_player_2


def selection_card(desc_player):           # вибір карти для роздачі
    cards_player = desc_player[0]
    return cards_player           # ?????????????????



def  wins_player(player_a, player_b, desc_player):   # забирає виграні карти
    desc_player = desc_player.appennd(player_a, player_b)
    return desc_player




# якщо буде час
def  add_compare_cards():   # спір на роздачі
    pass


"""

