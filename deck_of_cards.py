class Deck_of_cards:
    def __init__(self, name, rank, suits, picture, rating):
        self.name = name
        self.rank = rank
        self.suits = suits
        self.picture = picture
        self.rating = rating


    def rank_cards(self, cards_player):   # ранг карти з урахуванням мастей.
        rank_cards = self.rank + self.rating    # ще не додумав
        return rank_cards


"""
rank_of_cards = ["six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
card_suit =["spades", "clubs", "diamonds", "hearts"]

# створив змінні, назви карт
def cards_and_suits(a, b):
    y = 5
    for i in a :
        y += 1
        z = 0.1
        for x in b:
           z = round(z+0.1, 2)
           #desk_of_cards.push(Deck_of_cards f"{i}_{x} = Deck_of_cards('{i}_{x}', {y}, '{x}','link', {z})")
           #print(f"{i}_{x} = Deck_of_cards('{i}_{x}', {y}, '{x}','link', {z})")
           print(f"{i}_{x}")

cards_and_suits(rank_of_cards, card_suit)"""


six_spades = Deck_of_cards('six_spades', 6, 'spades','link', 0.2)
six_clubs = Deck_of_cards('six_clubs', 6, 'clubs','link', 0.3)
six_diamonds = Deck_of_cards('six_diamonds', 6, 'diamonds','link', 0.4)
six_hearts = Deck_of_cards('six_hearts', 6, 'hearts','link', 0.5)
seven_spades = Deck_of_cards('seven_spades', 7, 'spades','link', 0.2)
seven_clubs = Deck_of_cards('seven_clubs', 7, 'clubs','link', 0.3)
seven_diamonds = Deck_of_cards('seven_diamonds', 7, 'diamonds','link', 0.4)
seven_hearts = Deck_of_cards('seven_hearts', 7, 'hearts','link', 0.5)
eight_spades = Deck_of_cards('eight_spades', 8, 'spades','link', 0.2)
eight_clubs = Deck_of_cards('eight_clubs', 8, 'clubs','link', 0.3)
eight_diamonds = Deck_of_cards('eight_diamonds', 8, 'diamonds','link', 0.4)
eight_hearts = Deck_of_cards('eight_hearts', 8, 'hearts','link', 0.5)
nine_spades = Deck_of_cards('nine_spades', 9, 'spades','link', 0.2)
nine_clubs = Deck_of_cards('nine_clubs', 9, 'clubs','link', 0.3)
nine_diamonds = Deck_of_cards('nine_diamonds', 9, 'diamonds','link', 0.4)
nine_hearts = Deck_of_cards('nine_hearts', 9, 'hearts','link', 0.5)
ten_spades = Deck_of_cards('ten_spades', 10, 'spades','link', 0.2)
ten_clubs = Deck_of_cards('ten_clubs', 10, 'clubs','link', 0.3)
ten_diamonds = Deck_of_cards('ten_diamonds', 10, 'diamonds','link', 0.4)
ten_hearts = Deck_of_cards('ten_hearts', 10, 'hearts','link', 0.5)
jack_spades = Deck_of_cards('jack_spades', 11, 'spades','link', 0.2)
jack_clubs = Deck_of_cards('jack_clubs', 11, 'clubs','link', 0.3)
jack_diamonds = Deck_of_cards('jack_diamonds', 11, 'diamonds','link', 0.4)
jack_hearts = Deck_of_cards('jack_hearts', 11, 'hearts','link', 0.5)
queen_spades = Deck_of_cards('queen_spades', 12, 'spades','link', 0.2)
queen_clubs = Deck_of_cards('queen_clubs', 12, 'clubs','link', 0.3)
queen_diamonds = Deck_of_cards('queen_diamonds', 12, 'diamonds','link', 0.4)
queen_hearts = Deck_of_cards('queen_hearts', 12, 'hearts','link', 0.5)
king_spades = Deck_of_cards('king_spades', 13, 'spades','link', 0.2)
king_clubs = Deck_of_cards('king_clubs', 13, 'clubs','link', 0.3)
king_diamonds = Deck_of_cards('king_diamonds', 13, 'diamonds','link', 0.4)
king_hearts = Deck_of_cards('king_hearts', 13, 'hearts','link', 0.5)
ace_spades = Deck_of_cards('ace_spades', 14, 'spades','link', 0.2)
ace_clubs = Deck_of_cards('ace_clubs', 14, 'clubs','link', 0.3)
ace_diamonds = Deck_of_cards('ace_diamonds', 14, 'diamonds','link', 0.4)
ace_hearts = Deck_of_cards('ace_hearts', 14, 'hearts','link', 0.5)
