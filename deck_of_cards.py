def reading(file):
   filename = f'{file}'
   with open(filename) as file:
      c = file.read()
   return c.split(" ")


def cards_and_suits(rank, suit):
   desk_of_cards = []
   y = 5
   for i in rank:
      y += 1
      for x in suit:
         desk_of_cards.append([f'{i}', f'{x}'])
   return desk_of_cards


def selection_card(desc_player):  # вибір карти для роздачі
   cards_player = desc_player[0]
   desc_player.pop(0)
   return cards_player


def wins_player(player_a, player_b, desc_player):  # забирає виграні карти
   desc_player.append(player_a)
   desc_player.append(player_b)
   return desc_player
