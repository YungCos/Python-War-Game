# Miles Bernstien
# 2021-01-11
# War Code
# Plays the card game of war with a tkinter GUI

import War
import tkinter as tk

class GetNameUI:

    def window(self):

        #Create the window
        self.window = tk.Tk()
        self.window.title("War Game")
        self.window.resizable(False, False)

        #Create label
        tk.Label(self.window, text = 'Please Enter your name').pack()

        #Creates the Entry Box
        self.name = tk.Entry(self.window, width = 20)
        self.name.pack()

        #Creates the Confirm button
        tk.Button(self.window, text = "Confirm", command = self.quit).pack()

        #Runs the tkinter window
        self.window.mainloop()

        #Only runs when window is destroyed
        return self.userName

    #end window

    def quit(self):
        #Closes the window
        #No paramter
        #No return
        self.userName = self.name.get()

        #Change name if user hasn't inputted a name
        if self.userName == "":
            self.userName = "Player"

        self.window.destroy()
    #end quit
#end InstructionGUI

class MainMenu:
    def __init__(self):
        #Creates the main menu
        self.createMenu()

        #Initilizes the tkinter 
        self.window.mainloop()
    #end init

    def createMenu(self):
        # Creates main Tkinter elements
        # No paramters
        # No return

        #Create Window
        self.window = tk.Tk()
        self.window.title("War Game")
        self.window.resizable(False, False)

        #Create and pack Frames
        self.title = tk.Frame(self.window)
        self.options = tk.Frame(self.window)
        self.title.pack()
        self.options.pack()

        #Create Title Text
        self.titleText = tk.Label(self.title, text = "War Game")
        self.titleText.pack()

        #Create menu buttons
        self.playButton = tk.Button(self.options, text = "Play", command = self.startGame)
        self.instructions = tk.Button(self.options, text = "Instructions", command = self.showInstructions)
        self.quitButton = tk.Button(self.options, text = "Quit", command = self.quit)
        self.playButton.grid(row = 0, column = 0)
        self.instructions.grid(row = 0, column = 1)
        self.quitButton.grid(row = 0, column = 2)
    #end createMenu

    def startGame(self):
        # Activates when button is pressed, Initilizes war game
        # No paramters
        # No return

        #Destroys current main menu window
        self.window.destroy()

        #Creates two shuffled decks to be used in war
        deck1, deck2 = War.Deck().create().shuffle().split()

        #Returns the winner of the newly created war game
        playerWinner = CardGUI(deck1, deck2).winningPlayer

        #Exits if user exited game early
        if playerWinner is None:
            return

        #Recreate the main menu
        self.createMenu()

        #Changes the title text based on who won
        if playerWinner:
            self.titleText['text'] = 'You Won!'
        else:
            self.titleText['text'] = 'You Lost :('
        #end if

        # Runs main menu tkinter window
        self.window.mainloop()
    #end startGame

    def showInstructions(self):
        # Creates instruction window
        # No paramters
        # No return

        #Destroys main menu
        self.window.destroy()

        #Creates instruction window
        InstructionGUI()

        # Recreates main menu
        self.createMenu()
        self.window.mainloop()
    #end showInstructions

    def quit(self):
        #Destroys the window
        self.window.destroy()
#end MainMenu

class CardGUI:
    def __init__(self, deck1, deck2):
        self.isWar = False

        #Gets the name from the user
        self.userName = GetNameUI().window()

        #Creates instance of war game
        self.war = War.WarGame(deck1, deck2)
        
        #Creates decks
        self.deck1 = deck1
        self.deck2 = deck2

        #Creates window
        self.window = tk.Tk()
        self.window.title("War Game")
        self.window.resizable(False, False)

        #Creates frames
        self.score = tk.Frame(self.window)
        self.cards = tk.Frame(self.window, width = 150, height = 300)  
        self.cardFrame = tk.Frame(self.cards)
        self.next = tk.Frame(self.window)

        #Ensures the card frame remains a fixed size
        self.cards.grid_propagate(False)

        #Packs the frames
        self.score.grid(row = 0, column = 0)
        self.cards.grid(row = 0, column = 1)
        self.next.grid(row = 0, column = 2)
        self.cardFrame.grid(row = 1, column = 0)

        #Creates the UI elements
        self.createMenuBar()
        self.createElements()
        self.createCards()
        self.makeButton()

        #Starts the game
        self.update()

        #Runs the tkinter window
        self.window.mainloop()
    #end init

    def createMenuBar(self):
        # Creates the menu bar
        # No paramter
        # No return

        menubar = tk.Menu(self.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Instructions", command=InstructionGUI)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)

        self.window.config(menu=menubar)     
    #end createMenuBar

    def createElements(self):
        #Creates the score elements of the card ui
        # no paramaters
        # no return

        #Creates and packs placeholder labels to be changed
        self.playerName = tk.Label(self.score, borderwidth=2, relief="ridge", text = self.userName)
        self.playerScore = tk.Label(self.score, borderwidth=2, relief="ridge",text = "PLACEHOLDER")
        self.compName = tk.Label(self.score, borderwidth=2, relief="ridge",text = "Computer")
        self.compScore = tk.Label(self.score, borderwidth=2, relief="ridge",text = "PLACEHOLDER")
        self.playerName.pack()
        self.playerScore.pack()
        self.compName.pack()
        self.compScore.pack()
    #end createElements

    def createCards(self):
        #Create the elements for the cards frame
        # No paramters
        # No return

        #Creates the card templates
        self.playerTopCard = tk.PhotoImage(file = self.deck1.topCardFile(self.isWar))
        self.AITopCard = tk.PhotoImage(file = self.deck2.topCardFile(self.isWar))
        self.blankTemplate = tk.PhotoImage(file = "Cards/blank.png")

        #Creates The top text
        self.topText = tk.Label(self.cards, wraplength = 140,borderwidth=2, relief="ridge", height = 3, text = "Sample Text")

        #Creates the card image labels
        self.blankCardPlayer = tk.Label(self.cardFrame, image = self.blankTemplate)
        self.blankCardAI = tk.Label(self.cardFrame, image = self.blankTemplate)
        self.currCardPlayer = tk.Label(self.cardFrame, image = self.playerTopCard)
        self.currCardAI = tk.Label(self.cardFrame, image = self.AITopCard)

        #Creates the bottom text
        self.bottomText = tk.Label(self.cards, wraplength = 140,borderwidth=2, relief="ridge", text = "Sample Text")

        #Packs all the elements
        self.topText.grid(row = 0, column = 0)
        self.blankCardPlayer.grid(row = 1, column = 0)
        self.blankCardAI.grid(row = 2, column = 0)
        self.currCardPlayer.grid(row = 1, column = 1)
        self.currCardAI.grid(row = 2, column = 1)
        self.bottomText.grid(row = 3, column = 0)
    #end createCards

    def makeButton(self):
        # Create the button for the 'next' frame
        # no paramters
        # no return

        #Creates the button
        self.nextButton = tk.Button(self.next, text = "Next", command = self.update)
        self.nextButton.pack(side = 'top')
    #end makeButton

    def update(self):
        # Runs one cycle of the war game, called when user clicks next
        # No paramters
        # Returns whether the player won as a bool if applciable, if not there is no return

        #Checks if player or computer has won
        if self.hasWon():

            #Set the bool of the winning player (true = player, false = computer)
            self.winningPlayer = len(self.deck1.cards) > len(self.deck2.cards)

            #Destroys the tkinter window
            self.window.destroy()

        #end if

        #Gets the card files of the current top cards
        self.getCurrentCardFiles()

        #Determines the winner of the current two top cards and updates the decks accordingly
        self.deck1, self.deck2, self.playerWinner, self.isWar = self.war.doCycle()

        #Updates the UI
        self.updateText()
        self.updateCards()

    def updateText(self):
        # Updates the text of the score and the top and bottom text
        # no paramaters
        # no return

        #Changes the scores to the length of each deck
        self.playerScore['text'] = str(len(self.deck1.cards))
        self.compScore['text'] = str(len(self.deck2.cards))

        #Changes the top and bottom text based on the cards played and the player that won
        self.topText['text'] = self.higherText()
        self.bottomText['text'] = self.getWinnerText()
    #end updateText

    def higherText(self):
        #Returns what the top text should be
        # no paramaters
        # Return the text as a string to be used on the top

        #Runs if it's a war
        if self.isWar:
            return 'WAR!'

        #Runs if the player won
        elif self.playerWinner:
            return f'{self.war.deck1Card} is higher then {self.war.deck2Card}'

        #Runs if the computer won
        else:
            return f'{self.war.deck2Card} is higher then {self.war.deck1Card}'
        #end if
    #end higherText

    def getWinnerText(self):
        # Gets the text to be displayed on the bottom
        # No paramters
        # Return the text as a string to be used on the bottom

        #Checks if its's a war
        if self.isWar:

            #Runs if either player will have to play the rest of their cards during the war
            if len(self.deck1.cards) <=3 or len(self.deck2.cards) <= 3:
                return 'This is for the win!'

            #Runs If not displays the amount of cards can be won
            else:
                return f'There are {len(self.war.winnings) + 6} cards up for grabs'
            #end if

        #Checks if the player has won a war by checking they won more than 2 cards
        elif len(self.war.winnings) > 2:

            #Runs if player has won
            if self.playerWinner:
                return f'The player has won {len(self.war.winnings)} cards'
            
            #Runs if computer has won
            else:
                return f'The Computer has won {len(self.war.winnings)} cards'
            #end if
        
        #Runs if the player has won not through a war
        elif self.playerWinner:
            return f'The player has won the {self.deck1.cards[-1]}'
        #Runs if computer has won not through a war
        else:
            return f'The Computer has won the {self.deck2.cards[-2]}'
        #end if
    #end getWinnerText

    def updateCards(self):
        #Updates the cards image files
        #No paramters
        #No return

        #Updates the cards image files
        self.currCardPlayer['image'] = self.playerTopCard
        self.currCardAI['image'] = self.AITopCard
    #end updateCards

    def getCurrentCardFiles(self):
        #Gets the cards image files
        #No paramters
        #No return

        #Gets the cards image files
        self.playerTopCard = tk.PhotoImage(file = self.deck1.topCardFile(self.isWar))
        self.AITopCard = tk.PhotoImage(file = self.deck2.topCardFile(self.isWar))
    #end getCurrentCardFiles

    def hasWon(self):
        #Checks if user has won
        #No paramter
        #Retuns bool if player has won (player won = true, computer won = false)
        return len(self.deck1.cards) <= 0 or len(self.deck2.cards) <= 0
    #end hasWon

    def quit(self):
        #Destorys the window
        #No paramters
        #No return
        self.winningPlayer = None
        self.window.destroy()

#end CardGUI

class InstructionGUI:

    def __init__(self):
        #Create the window
        self.window = tk.Tk()
        self.window.title("War Game")
        self.window.resizable(False, False)

        #Creates the instructions label
        tk.Label(self.window, wraplength = 400, text = "Welcome To War!, Each player will flip a card and the player with the higher card value wins (ace high). If both players draw the same value, a war is started and both player will draw 3 more cards. The player with the higher value card on the third card will win the orignal card along with all the 3 other cards that were drawn for the war. If both cards are the same again, another war will take place. The game is won has won all the cards in the deck").pack()

        #Creates the back button
        tk.Button(self.window, text = "Back", command = self.quit).pack()

        #Runs the tkinter window
        self.window.mainloop()
    #end init

    def quit(self):
        #Closes the window
        #No paramter
        #No return
        self.window.destroy()
    #end quit
#end InstructionGUI

#Starts the main menu
MainMenu()