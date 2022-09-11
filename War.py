import random

class Card:
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    #end init

    def numToSuit(self):
        # Converts the suit intger to a string
        # No paramter
        # Returns string of the suits

        return self.suits[self.suit - 1]
    #end numToSuit

    def __str__(self):
        #Returns string formatted as 'NUMBER of SUIT'
        #No paramater
        #Returns string of formatted card
        return f"{self.numbers[self.number - 1]} of {self.suits[self.suit - 1]}"
    #end str
#end Card

class Deck:

    def __init__(self, cards = []):
        self.cards = cards
    #end init

    def create(self):
        # Creates a new deck
        # No paramters
        # returns the created deck


        self.cards = []

        #Loop through all possible card numbers
        for num in range(1, 14):
            #Loop through all possible suits
            for suit in range(1, 5):
                #Creates a new card
                self.cards += [Card(num, suit)]
            #end for
        #end for
        return self
    #end create

    def shuffle(self):
        # Shuffles the deck
        # No paramter
        # Returns the deck
        random.shuffle(self.cards)
        return self
    #end shuffle

    def split(self):
        # Splits the deck in two
        # No paramters
        # Returns 2 decks
        amount = len(self.cards)
        return Deck(self.cards[:amount // 2]), Deck(self.cards[amount//2:])
    #end split

    def nextCard(self):
        # Pops the first card in the deck and returns it 
        # No paramters
        # Returns the top card
        return self.cards.pop(0)
    #end nextCard

    def hasCards(self):
        # Checks if the deck has has cards
        # No paramters
        # Returns bool whether the deck has cards
        return len(self.cards) > 0
    #end hasCards

    def topCardFile(self, isWar):
        # Gets the file name of the card to be played by formatting Card types into strings
        # isWar is a bool that checks wheter it's a war
        # Returns the file name string of the card to be played
        
        #Checks if there's a war
        if isWar:
            #Runs if deck has less then 3 cards
            if len(self.cards) < 3:

                #Gets the last card
                number = self.cards[-1].number + 1
                suit = self.cards[-1].numToSuit().lower()
            #Runs if deck has at least 3 cards
            else:

                #Gets the third card
                number = self.cards[2].number + 1
                suit = self.cards[2].numToSuit().lower()
            #end if
        else:
            #Gets the top card
            number = self.cards[0].number + 1
            suit = self.cards[0].numToSuit().lower()
        #end if

        return f"Cards/{number}-{suit}.png"
    #end topCardFile
#end Deck

class WarGame:


    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.isWar = False
    #end init

    def getWinnings(self):
        #Determine the cards to be won by the winner
        # No paramters
        # No return

        #Runs if it's a war
        if self.isWar:

            #Loops three times through deck1
            for i in range(3):

                #Ensures deck is not empty
                if self.deck1.hasCards():

                    #Adds top to deck
                    self.winnings.append(self.deck1.nextCard())

                    #Sets the current card as the top card
                    self.deck1Card = self.winnings[-1]
                #end if
            #end for
            
            #Loops three times through deck2
            for i in range(3):

                #Ensures deck is not empty
                if self.deck2.hasCards():

                    #Adds top to deck
                    self.winnings.append(self.deck2.nextCard())

                    #Sets the current card as the top card
                    self.deck2Card = self.winnings[-1]
                #end if
            #end for

        #Runs if its not a war
        else:
            #Gets the top card of each deck
            self.deck1Card = self.deck1.nextCard()
            self.deck2Card = self.deck2.nextCard()

            #Sets those cards to the new winnings
            self.winnings = [self.deck1Card, self.deck2Card]
        #end if

        return self.winnings
    #end getWinnings

    def doCycle(self):
        #Does one turn of the war game
        # No paramters
        # reutns the updated decks after the turn, the winner and whether it's a war

        #Gets list of current winnings
        self.winnings = self.getWinnings()

        #Sets isWar to false by default
        self.isWar = False

        #Checks if player 1's card is higher
        if self.deck1Card.number > self.deck2Card.number:

            #Adds winnings to deck1
            self.deck1.cards += self.winnings

            #Declares the player is is the winner
            playerWinner = True
        
        #Checks if player 2's card is higher
        elif self.deck2Card.number > self.deck1Card.number:
            #Adds winnings to deck1
            self.deck2.cards += self.winnings

            #Declares the player is is the loser
            playerWinner = False

        #Runs when both card values are the same
        else:
            #There is no winner or l
            playerWinner = None

            #Both cards are the same, so it's a war
            self.isWar = True
        #end if

        return self.deck1, self.deck2, playerWinner, self.isWar
    #end doCycle
#end WarGame