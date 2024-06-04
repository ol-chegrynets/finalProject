import random





desc_player_1 = []      # колода гравця 1
desc_player_2 = []      # колода гравця 2


cards_player_1 = 0      # карта на роздачі гравця 1
cards_player_2 = 0      # карта на роздачі гравця 2






class Deck_of_cards:

    spades = 100
    clubs = 200
    diamonds = 300
    hearts = 400
    def __init__(self):
        self.rank_of_cards = ["six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
        self.card_suit = ["spades", "clubs", "diamonds", "hearts"]
        self.rank = 0
        self.suits = 0
        self.desk_of_cards = []


"""
    y = 5
    for i in self.rank_of_cards:
        y += 1
        for x in self.card_suit:
            self.desk_of_cards.append(['1', '{x}']")
    print(self.desk_of_cards)"""

    def distribution_of_cards(self):  # розділ колоди на 2 частини
        division_cargs =0

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

        # print(len(desc_player_1), desc_player_1)
        # print(len(desc_player_2), desc_player_2)
        return desc_player_1, desc_player_2

    def card_picture(self):     # додати link на зображення
        pass

    def rank_cards(self, cards_player):   # ранг карти з урахуванням мастей.
        print(cards_player.rank)
        rank_card = cards_player.rank + cards_player.suit
        print(rank_card)
        #rank_cards = cards_player.rank + cards_player.suits   # ще не додумав
        return rank_card

    def compare_cards(self, cards_player_1, cards_player_2):  # порівняти карти на роздачі

        if self.rank_cards(cards_player_1) < self.rank_cards(cards_player_2):   #??????  метод класу
            wins_player(cards_player_1, cards_player_2, desc_player_1)
            print(wins_player(cards_player_1, cards_player_2, desc_player_1))
        else:
            wins_player(cards_player_2, cards_player_1, desc_player_2)
            print(wins_player(cards_player_2, cards_player_1, desc_player_2))
        # if rank_cards_play_1 = rank_cards_play_2:   add_compare_cards()

    def __str__(self):
        return " hello"




def name_player():      #  додавання ім'я ігрока
    name_player_1 = input("Enter name player 1: ")
    name_player_2 = input("Enter name player 2: ")

def exit_game():     # преривання гри на вимогу, наприклад клав."esc"
    pass



# def visual_distrib():        # вызуальне роздавання карт на двох.
#    pass



def loop():
    print("Hello1")
    while (len(desc_player_1) != 0 and len(desc_player_2) != 0):
        print("Hello1")




def selection_card(desc_player):           # вибір карти для роздачі
    cards_player = desc_player[0]
    desc_player.pop(0)
    return cards_player


def put_card():     # покласти карту на роздчу
    global cards_player_1, cards_player_2
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
            x = 1
        elif  pres_button == "l":
            cards_player_2 = selection_card(desc_player_2)
            y = 1

    return cards_player_1, cards_player_2





def  wins_player(player_a, player_b, desc_player):   # забирає виграні карти
    desc_player = desc_player.appennd(player_a, player_b)
    return desc_player




# якщо буде час
"""def  add_compare_cards():   # спір на роздачі
    pass"""

#================================begin=========================

#desk_of_cards = {'six_spades':Deck_of_cards(6, 'spades'), 'six_clubs': Deck_of_cards(6, 'clubs'), 'six_diamonds': Deck_of_cards(6, 'diamonds'), 'six_hearts':Deck_of_cards(6, 'hearts'), 'seven_spades': Deck_of_cards(7, 'spades'), 'seven_clubs':Deck_of_cards(7, 'clubs'), 'seven_diamonds':Deck_of_cards(7, 'diamonds'), 'seven_hearts':Deck_of_cards(7, 'hearts') }

game = Deck_of_cards()



print(game)




#cards_and_suits(rank_of_cards, card_suit)
#name_player()




#distribution_of_cards(desk_of_cards)       # доробить перемішування колоди через інший метод

#put_card()
#print('kjgjh', cards_player_1)
#Deck_of_cards.compare_cards(1,cards_player_1, cards_player_2)  # self????


#Deck_of_cards.rank_cards(six_spades = Deck_of_cards(6, 'spades'))




"""    не працює    """

