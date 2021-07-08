class Player:

    def __init__(self, name):
        self.card_hand = []
        self.name = name

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.card_hand.extend(new_cards)
        else:
            self.card_hand.append(new_cards)

    def remove_cards(self, cards):
        self.card_hand.pop(cards)

'''
#idea for changing hands in poker with 5 cards each

listone = [1,2,3,4]
removelist = [3,4]

for x in range(len(removelist)):
    listone.remove(removelist[x])

print(listone)
'''
