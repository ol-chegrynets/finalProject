# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




import random
y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
desc_player_1 = []
desc_player_2 = []
cards_player_1 = 0
cards_player_2 = 0
cards_player = []

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


distribution_of_cards(y)


print(len(desc_player_1),desc_player_1)
print(len(desc_player_2),desc_player_2)



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
            #print("1",cards_player_1)
            x = 1
            continue
        elif  pres_button == "l":
                cards_player_2 = selection_card(desc_player_2)
                #print("2",cards_player_2)
                y = 1
                continue




def selection_card(desc_player):           # вибір карти для роздачі
    cards_player = desc_player[0]
    desc_player.pop(0)
    return cards_player

put_card()

print(len(desc_player_1),desc_player_1)
print(len(desc_player_2),desc_player_2)
print(cards_player_1)
print(cards_player_2)
