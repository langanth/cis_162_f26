
class Card:

    def __init__(self, value, rank, suit):
        '''self.set_value(value)
        self.set_rank(rank)
        self.set_suit(suit)'''

        '''if not isinstance(value, int):
            raise TypeError
        if not 1 <= value <= 10:
            raise ValueError'''

        self.set_value(value)
        if not isinstance(rank, int):
            raise TypeError
        if not 1 <= rank <= 13:
            raise ValueError
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        if not isinstance(suit, str):
            raise TypeError
        if suit not in suits:
            raise ValueError

        self.value = value
        self.suit = suit
        self.rank = rank

    def set_value(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not 1 <= value <= 10:
            raise ValueError
        self.value = value

if __name__ == "__main__":
    ui = ''
    deck = []

    while ui != "QUIT":
        try:
            val = int(input("Please enter a card value: "))
            rank = int(input("Please enter a rank value: "))
            suit = input("Please enter a suit: ")
            new_card = Card(val, rank, suit)
            deck.append(new_card)
            ui = input("Continue?: ")
        except:
            print("oops")
            print("please try again!")