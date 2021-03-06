class Card:
    def __init__(self,value,suit):
        # if value of card is not a number, error will appear
        if type(value) is not int:
            raise TypeError('invalid type')
        # if value of card is out of range, error will appear
        elif 2>value or value>14:
            raise ValueError('invalid value')
        else:
            self.value=value
        # if suit of card is not valid, error will appear
        if suit in ['♥','♠','🔶','♣']:
            self.suit = suit
        else:
            raise ('invalid suit type for card')
        self.value_names = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 'Jack', 12: 'Queen', 13: 'King',14: 'Ace'}

    # a method that checks which card is bigger, depends on value and suit
    def __gt__(self, other):
        rules={'♥':1,'♠':2,'🔶':3,'♣':4}

        # compares values and suit of two cards
        if self.value == other.value:
           if rules[self.suit] > rules[other.suit]:
               return True
           else:
               return False

        elif self.value > other.value:
            return True
        else:
            return False

    # a method that return printable values
    def __repr__(self):
        return f"{self.value_names[self.value]} {self.suit}"

    # a method that compares two equal cards
    def __eq__(self, other):
        if type(other) != Card:
            raise TypeError('invalid type of argument for card')
        if self.suit == other.suit and self.value == other.value:
            return True
        return False