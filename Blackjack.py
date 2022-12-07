import random
import tkinter


def start():
    for i in range(2):
        card = random.choice(Blackjack.deck)
        Blackjack.playerHand.append(card)
        Blackjack.deck.remove(card)
        card = random.choice(Blackjack.deck)
        Blackjack.dealerHand.append(card)
        Blackjack.deck.remove(card)
    print(f'Your hand:{Blackjack.playerHand[0]}, {Blackjack.playerHand[1]}')
    print(f'Dealer hand: {Blackjack.dealerHand[0]}')


# reset function
def reset():
    # reset deck into the default full deck
    Blackjack.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
                      2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
                      2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
                      2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    Blackjack.playerHand = []
    Blackjack.dealerHand = []


def fold():
    print("You Fold")
    reset()
    start()


# deal player a card
def dealPlayerCard():
    # random card from deck
    card = random.choice(Blackjack.deck)
    # deal to player and remove from deck
    Blackjack.playerHand.append(card)
    Blackjack.deck.remove(card)
    print(f'Your hand: {Blackjack.playerHand}')
    calculatePlayerHand()


# deal dealer a card
def dealDealerCard():
    # random card from deck
    card = random.choice(Blackjack.deck)
    # deal to dealer and remove from deck
    Blackjack.dealerHand.append(card)
    Blackjack.deck.remove(card)
    print(f'Dealer hand: {Blackjack.dealerHand}')
    calculateDealerHand()


def calculatePlayerHand():
    total = 0
    face = ["J", "Q", "K"]
    for card in Blackjack.playerHand:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        elif card == "A":
            total += 11
    if total == 21:
        print("Blackjack! You win!")
        print(f'Your total: {total}')
        reset()
    elif total > 21:
        print("Bust! You lose!")
        print(f'Your total: {total}')
        reset()


def calculateDealerHand():
    total = 0
    face = ["J", "Q", "K"]
    for card in Blackjack.dealerHand:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        elif card == "A":
            total += 11
    if total == 21:
        print("Dealer Blackjack! You lose")
        print(f'Dealer total: {total}')
        reset()
    elif total > 21:
        print("Dealer Bust! You win!")
        print(f'Dealer total: {total}')
        reset()


class Blackjack:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
            2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
            2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K',
            2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    playerHand = []
    dealerHand = []

    def __init__(self):
        # basic GUI setup
        self.root = tkinter.Tk()
        self.root.geometry("800x500")
        self.root.title("blackjack")
        self.label = tkinter.Label(self.root, text="🎰 Blackjack 🪙", font=('Arial', 26))
        self.label.pack(padx=20, pady=20)
        self.root['background'] = "#516646"

        # button setup
        self.buttonFrame = tkinter.Frame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)
        self.buttonFrame.columnconfigure(3, weight=1)

        # play buttons
        self.stand = tkinter.Button(self.buttonFrame, bg="#852928", fg='white',
                                    text='Stand', font=('Arial', 16), command=dealDealerCard)
        self.stand.grid(row=0, column=0, sticky=tkinter.W + tkinter.E)
        self.hit = tkinter.Button(self.buttonFrame, bg="black", fg='white',
                                  text='Hit', font=('Arial', 16), command=dealPlayerCard)
        self.hit.grid(row=0, column=1, sticky=tkinter.W + tkinter.E)
        self.double = tkinter.Button(self.buttonFrame, bg="#852928", fg='white',
                                     text='Double', font=('Arial', 16))
        self.double.grid(row=0, column=2, sticky=tkinter.W + tkinter.E)
        self.fold = tkinter.Button(self.buttonFrame, bg="black", fg='white',
                                   text='Fold', font=('Arial', 16), command=fold)
        self.fold.grid(row=0, column=3, sticky=tkinter.W + tkinter.E)
        self.buttonFrame.pack(fill='x')

        # menu buttons
        self.startButton = tkinter.Button(self.root, text="START", command=self.gameStart)
        self.startButton.place(x=0, y=0, height=50, width=100)
        self.endButton = tkinter.Button(self.root, text="END", command=self.gameEnd)
        self.endButton.place(x=100, y=0, height=50, width=100)

        # default state of buttons
        self.stand["state"] = "disabled"
        self.hit["state"] = "disabled"
        self.double["state"] = "disabled"
        self.fold["state"] = "disabled"
        self.startButton["state"] = "normal"

        self.root.mainloop()

    # game start function
    def gameStart(self):
        # enables buttons
        self.stand["state"] = "normal"
        self.hit["state"] = "normal"
        self.double["state"] = "normal"
        self.fold["state"] = "normal"
        self.startButton["state"] = "disabled"
        start()

    def gameEnd(self):
        self.stand["state"] = "disabled"
        self.hit["state"] = "disabled"
        self.double["state"] = "disabled"
        self.fold["state"] = "disabled"
        self.startButton["state"] = "normal"
        reset()


Blackjack()
