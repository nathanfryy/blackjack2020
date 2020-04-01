class Card(object):

    def __index__(self, name, suit):
        self.__name = name
        self.__suit = suit
        self.__value = self.card_Value(name)
        self.__visibility = False
        self.__suitUnicode = self.suit_Unicode(suit)
        self.__cardColor = self.card_Color(suit)

    def __str__(self):
        if self.__visibility == True:
            string = ''
            string += f'           Card    '
            string += f'---------------------------'
            string += f'Color: {self.__cardColor}'
            string += f'Suit:  {self.suit}'
            string += f'Value: {self.__value}'
            string += ''
            return string
        else:
            string = ''
            string += 'Sorry, you cannot see the card.'
            string += 'It is currently facing down.'
            string += ''
            return string


    def get__name(self):
        return self.__name

    def get__suit(self):
        return self.__suit

    def get__value(self):
        return self.__value

    def get_suitUnicode(self):
        return self.__suitUnicode

    def get_cardColor(self):
        return self.__cardColor

    def card_Value(self, name):
        if name == 'ace':
            return '1'
        elif name == 'two':
            return '2'
        elif name == 'three':
            return '3'
        elif name == 'four':
            return '4'
        elif name == 'five':
            return '5'
        elif name == 'six':
            return '6'
        elif name == 'seven':
            return '7'
        elif name == 'eight':
            return '8'
        elif name == 'nine':
            return '9'
        elif name == 'ten':
            return '10'
        elif name == 'jack':
            return 'Jack(10)'
        elif name == 'queen':
            return 'Queen(10)'
        elif name == 'king':
            return 'King(10)'

    def suit_Unicode(self, suit):
        if suit == 'spades':
            return f'\u2660'
        elif suit == 'clubs':
            return f'\u2663'
        elif suit == 'hearts':
            return f'\u2665'
        elif suit == 'diamonds':
            return f'\u2662'

    def card_Color(self, suit):
        if suit in ['spades', 'clubs']:
            self.__cardColor = 'black'
        elif suit in ['hearts', 'diamonds']:
            self.__cardColor = 'red'
        return self.__cardColor



