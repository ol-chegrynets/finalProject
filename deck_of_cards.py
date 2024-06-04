"""import game_functional
rank_of_cards = ["six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
card_suit = ["spades", "clubs", "diamonds", "hearts"]

desk_of_cards = ['six_spades', 'six_clubs', 'six_diamonds', 'six_hearts', 'seven_spades', 'seven_clubs', 'seven_diamonds', 'seven_hearts', 'eight_spades', 'eight_clubs', 'eight_diamonds', 'eight_hearts', 'nine_spades', 'nine_clubs', 'nine_diamonds', 'nine_hearts', 'ten_spades', 'ten_clubs', 'ten_diamonds', 'ten_hearts', 'jack_spades', 'jack_clubs', 'jack_diamonds', 'jack_hearts', 'queen_spades', 'queen_clubs', 'queen_diamonds', 'queen_hearts', 'king_spades', 'king_clubs', 'king_diamonds', 'king_hearts', 'ace_spades', 'ace_clubs', 'ace_diamonds', 'ace_hearts']
"""
"""
class Deck_of_cards:

    spades = 100
    clubs = 200
    diamonds = 300
    hearts = 400
    def __init__(self, rank, suits):
        self.rank = rank
        self.suits = suits


    def card_picture(self):     # додати link на зображення
        pass

    def rank_cards(self):   # ранг карти з урахуванням мастей.
        rank_cards = cards_player.rank + cards_player.suits   # ще не додумав
        return rank_cards

    def compare_cards(self, cards_player_1, cards_player_2):  # порівняти карти на роздачі
        if cards_player_1.rank < cards_player_2.rank:
            game_functional.wins_player(cards_player_1, cards_player_2, desc_player_1, desc_player_2)
            print(wins_player())
        else:
            game_functional.wins_player(cards_player_2, cards_player_1, desc_player_2, desc_player_1)
            print(wins_player())
        # if rank_cards_play_1 = rank_cards_play_2:   add_compare_cards()

""""""
#desk_of_cards = []

# створив змінні, назви карт
def cards_and_suits(a, b):
    y = 5
    for i in a :
        y += 1
        for x in b:
           ######desk_of_cards.append(Deck_of_cards f"{i}_{x} = Deck_of_cards({y}, '{x}','link')")
           print(f"{i}_{x} = Deck_of_cards({y}, '{x}')")
           #desk_of_cards.append(f"{i}_{x}")

cards_and_suits(rank_of_cards, card_suit)"""


"""
six_spades = Deck_of_cards(6, 'spades')
six_clubs = Deck_of_cards(6, 'clubs')
six_diamonds = Deck_of_cards(6, 'diamonds')
six_hearts = Deck_of_cards(6, 'hearts')
seven_spades = Deck_of_cards(7, 'spades')
seven_clubs = Deck_of_cards(7, 'clubs')
seven_diamonds = Deck_of_cards(7, 'diamonds')
seven_hearts = Deck_of_cards(7, 'hearts')
eight_spades = Deck_of_cards(8, 'spades')
eight_clubs = Deck_of_cards(8, 'clubs')
eight_diamonds = Deck_of_cards(8, 'diamonds')
eight_hearts = Deck_of_cards(8, 'hearts')
nine_spades = Deck_of_cards(9, 'spades')
nine_clubs = Deck_of_cards(9, 'clubs')
nine_diamonds = Deck_of_cards(9, 'diamonds')
nine_hearts = Deck_of_cards(9, 'hearts')
ten_spades = Deck_of_cards(10, 'spades')
ten_clubs = Deck_of_cards(10, 'clubs')
ten_diamonds = Deck_of_cards(10, 'diamonds')
ten_hearts = Deck_of_cards(10, 'hearts')
jack_spades = Deck_of_cards(11, 'spades')
jack_clubs = Deck_of_cards(11, 'clubs')
jack_diamonds = Deck_of_cards(11, 'diamonds')
jack_hearts = Deck_of_cards(11, 'hearts')
queen_spades = Deck_of_cards(12, 'spades')
queen_clubs = Deck_of_cards(12, 'clubs')
queen_diamonds = Deck_of_cards(12, 'diamonds')
queen_hearts = Deck_of_cards(12, 'hearts')
king_spades = Deck_of_cards(13, 'spades')
king_clubs = Deck_of_cards(13, 'clubs')
king_diamonds = Deck_of_cards(13, 'diamonds')
king_hearts = Deck_of_cards(13, 'hearts')
ace_spades = Deck_of_cards(14, 'spades')
ace_clubs = Deck_of_cards(14, 'clubs')
ace_diamonds = Deck_of_cards(14, 'diamonds')
ace_hearts = Deck_of_cards(14, 'hearts')


"""
