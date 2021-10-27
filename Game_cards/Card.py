class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
        self.full_card = [suit,value]

    # a method that checks which card is bigger, depends on value and suit
    def __gt__(self, other):
        rules={"Diamond":1,"Spade":2,"Heart":3,"Club":4}

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
        return f"{self.value} {self.suit}"


