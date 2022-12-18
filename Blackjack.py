import random
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

# initializing variables
deck = []
player = []
dealer = []
dealer_card_slots = 0
player_card_slots = 0
player_total = 0
dealer_total = 0


# refill deck function
def refill_deck():
    global deck
    deck = []
    # suits possible
    suits = ["diamonds", "clubs", "hearts", "spades"]
    # values possible
    values = range(2, 15)
    for suit in suits:
        for value in values:
            deck.append(f'{value}_of_{suit}')
    # reset image of dealer and player hands to nothing
    dealer_label_1.config(image='')
    dealer_label_2.config(image='')
    dealer_label_3.config(image='')
    dealer_label_4.config(image='')
    dealer_label_5.config(image='')

    player_label_1.config(image='')
    player_label_2.config(image='')
    player_label_3.config(image='')
    player_label_4.config(image='')
    player_label_5.config(image='')


# game start function
def game_start():
    # enables buttons
    stand["state"] = "normal"
    hit["state"] = "normal"
    fold["state"] = "normal"
    start_button["state"] = "disabled"
    start()


# game end function
def game_end():
    # disables buttons
    stand["state"] = "disabled"
    hit["state"] = "disabled"
    fold["state"] = "disabled"
    start_button["state"] = "normal"
    reset()


# start function
def start():
    global dealer, player
    dealer = []
    player = []

    # fills deck with cards
    refill_deck()

    # deals cards to dealer and player
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()

    # covers dealer's card
    hide_dealer_card()

    # if bust on starting hand, restart the game
    if calculate_player_hand() > 21 or calculate_dealer_hand() > 21:
        game_end()
        start()

    # if you blackjack then you blackjack
    elif calculate_player_hand() == 21 or calculate_dealer_hand() == 21:
        blackjack()
        disable_buttons()


# reset function
def reset():
    global player, dealer, player_card_slots, dealer_card_slots, player_total, dealer_total, player_value, dealer_value
    refill_deck()
    player_card_slots = 0
    dealer_card_slots = 0
    root.title(f'Blackjack')
    player = []
    dealer = []
    player_total = 0
    dealer_total = 0
    player_value = 0
    dealer_value = 0


def disable_buttons():
    fold["state"] = "disabled"
    hit["state"] = "disabled"
    stand["state"] = "disabled"


# deal player a card
def deal_player_card():
    global player_card_slots
    # max card slots is 5
    if player_card_slots < 5:
        # try except statement for if you run out of cards
        try:
            # at random choose a card from deck
            player_card = random.choice(deck)
            # remove that card from deck and append it to your hand
            deck.remove(player_card)
            player.append(player_card)

            global player_image_1, player_image_2, player_image_3, player_image_4, player_image_5
            calculate_player_hand()

            # if at card slot x, then label x is where your image will be, and then increment to the next card slot
            if player_card_slots == 0:
                player_image_1 = resize_cards(f'deck/{player_card}.png')
                player_label_1.config(image=player_image_1)
                player_card_slots += 1
            elif player_card_slots == 1:
                player_image_2 = resize_cards(f'deck/{player_card}.png')
                player_label_2.config(image=player_image_2)
                player_card_slots += 1
            elif player_card_slots == 2:
                player_image_3 = resize_cards(f'deck/{player_card}.png')
                player_label_3.config(image=player_image_3)
                # disable fold option after hit
                fold["state"] = "disabled"
                player_card_slots += 1
            elif player_card_slots == 3:
                player_image_4 = resize_cards(f'deck/{player_card}.png')
                player_label_4.config(image=player_image_4)
                player_card_slots += 1
            elif player_card_slots == 4:
                player_image_5 = resize_cards(f'deck/{player_card}.png')
                player_label_5.config(image=player_image_5)
                player_card_slots += 1
            # title of interface displays how many cards left in deck
            root.title(f'Blackjack - {len(deck)} cards left')
        except:
            root.title(f'Blackjack - No Cards Left')


# deal dealer a card
def deal_dealer_card():
    global dealer_card_slots
    # max card slots is 5
    if dealer_card_slots < 5:
        # try except statement for if you run out of cards
        try:
            # at random choose a card from deck
            dealer_card = random.choice(deck)
            # remove that card from deck and append it to your hand
            deck.remove(dealer_card)
            dealer.append(dealer_card)

            global dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5
            calculate_dealer_hand()

            # if at card slot x, then label x is where your image will be, and then increment to the next card slot
            if dealer_card_slots == 0:
                dealer_image_1 = resize_cards(f'deck/{dealer_card}.png')
                dealer_label_1.config(image=dealer_image_1)
                dealer_card_slots += 1
            elif dealer_card_slots == 1:
                dealer_image_2 = resize_cards(f'deck/{dealer_card}.png')
                dealer_label_2.config(image=dealer_image_2)
                dealer_card_slots += 1
            elif dealer_card_slots == 2:
                dealer_image_3 = resize_cards(f'deck/{dealer_card}.png')
                dealer_label_3.config(image=dealer_image_3)
                # disable fold and hit options after standing
                dealer_card_slots += 1
            elif dealer_card_slots == 3:
                dealer_image_4 = resize_cards(f'deck/{dealer_card}.png')
                dealer_label_4.config(image=dealer_image_4)
                dealer_card_slots += 1
            elif dealer_card_slots == 4:
                dealer_image_5 = resize_cards(f'deck/{dealer_card}.png')
                dealer_label_5.config(image=dealer_image_5)
                dealer_card_slots += 1
            root.title(f'Blackjack - {len(deck)} cards left')
        except:
            root.title(f'Blackjack - No Cards Left')


# resizing the card images
def resize_cards(card):
    card_image = Image.open(card)

    # resizing image
    card_image_resize = card_image.resize((113, 164))
    global card_img
    card_img = ImageTk.PhotoImage(card_image_resize)
    return card_img


def fold_function():
    reset()
    # deal new cards
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()
    # hide dealer card
    hide_dealer_card()


def stand_function():
    # show dealer's hidden card
    reveal_dealer_card()
    # disable buttons
    disable_buttons()
    # if dealer total is less than 17 then draw cards
    while calculate_dealer_hand() < 17:
        deal_dealer_card()
    # if dealer hand is above 17, now start counting scores
    if calculate_dealer_hand() >= 17:
        # blackjack condition
        if calculate_dealer_hand() == 21:
            blackjack()
        # bust condition
        elif calculate_dealer_hand() > 21:
            bust()
        # dealer win condition
        elif calculate_player_hand() < calculate_dealer_hand() < 21:
            reveal_dealer_card()
            messagebox.showinfo('Lose', 'You Lose!')
        # player win condition
        elif calculate_dealer_hand() < calculate_player_hand() < 21:
            reveal_dealer_card()
            messagebox.showinfo('Win', 'You Win!')
        # draw condition
        elif calculate_player_hand() == calculate_player_hand():
            reveal_dealer_card()
            messagebox.showinfo('Draw', 'Draw')


def hit_function():
    deal_player_card()
    hide_dealer_card()
    # if your hand is 21, blackjack
    if calculate_player_hand() == 21:
        blackjack()
        disable_buttons()
    # if your hand is above 21, bust
    elif calculate_player_hand() > 21:
        bust()
        disable_buttons()


def calculate_player_hand():
    global player_total, player
    # if the total of your hand is 0 just reset it back to zero for calculation purposes
    if player_total != 0:
        player_total = 0
    # for card in your hand, split the name of your card and take just the number
    # add up scores accordingly to the name of the card in your hand
    for c in player:
        value = int(c.split("_")[0])
        if value in range(2, 11):
            player_total += value
        elif value in range(11, 14):
            player_total += 10
        elif value == 14:
            player_total += 11

    return player_total


def calculate_dealer_hand():
    global dealer_total, dealer
    # if the total of dealer hand is 0 just reset it back to zero for calculation purposes
    if dealer_total != 0:
        dealer_total = 0
    # for card in dealer hand, split the name of dealer card and take just the number
    # add up scores accordingly to the name of the card in dealer hand
    for c in dealer:
        value = int(c.split("_")[0])
        if value in range(2, 11):
            dealer_total += value
        elif value in range(11, 14):
            dealer_total += 10
        elif value == 14:
            dealer_total += 11

    return dealer_total


def blackjack():
    # reveal dealer's hidden card
    reveal_dealer_card()
    # if both hands are blackjack then you draw
    if calculate_dealer_hand() == 21 and calculate_player_hand() == 21:
        messagebox.showinfo('Draw', 'Draw')
    # if dealer blackjack
    elif calculate_dealer_hand() == 21:
        messagebox.showinfo('Blackjack', 'Oh no! Dealer blackjack!')
    # if you blackjack
    elif calculate_player_hand() == 21:
        messagebox.showinfo('Blackjack', 'Congratulations! Blackjack!')


def bust():
    reveal_dealer_card()
    # if dealer bust
    if calculate_dealer_hand() > 21:
        messagebox.showinfo('Bust', 'Dealer bust! Very nice!')
    # if player bust
    elif calculate_player_hand() > 21:
        messagebox.showinfo('Bust', 'Oh no! You bust!')


# hide dealer's second card
def hide_dealer_card():
    dealer_image_2 = resize_cards('deck/cardback.png')
    dealer_label_2.config(image=dealer_image_2)


# reveal dealer's second card
def reveal_dealer_card():
    dealer_image_2 = resize_cards(f'deck/{dealer[1]}.png')
    dealer_label_2.config(image=dealer_image_2)


# basic GUI setup
root = tkinter.Tk()
root.geometry("1000x800")
root.title("Blackjack")
label = tkinter.Label(root, text="🎰 Blackjack 🪙", font=('Arial', 26))
label.pack(padx=20, pady=20)
root['background'] = "#516646"
root.iconbitmap("icon\poker_icon.ico")

# button setup
buttonFrame = tkinter.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

# play buttons
stand = tkinter.Button(buttonFrame, bg="#852928", fg='white',
                       text='Stand', font=('Arial', 16), command=stand_function)
stand.grid(row=0, column=0, sticky=tkinter.W + tkinter.E)

hit = tkinter.Button(buttonFrame, bg="black", fg='white',
                     text='Hit', font=('Arial', 16), command=hit_function)
hit.grid(row=0, column=1, sticky=tkinter.W + tkinter.E)

fold = tkinter.Button(buttonFrame, bg="#852928", fg='white',
                      text='Fold', font=('Arial', 16), command=fold_function)
fold.grid(row=0, column=2, sticky=tkinter.W + tkinter.E)

buttonFrame.pack(fill='x')

# Frame for cards
my_frame = tkinter.Frame(root, bg="#516646")
my_frame.pack(pady=20)

dealer_frame = tkinter.LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = tkinter.LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(pady=10, ipadx=20)

# Labels for dealer cards
dealer_label_1 = tkinter.Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = tkinter.Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = tkinter.Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)

dealer_label_4 = tkinter.Label(dealer_frame, text='')
dealer_label_4.grid(row=0, column=3, pady=20, padx=20)

dealer_label_5 = tkinter.Label(dealer_frame, text='')
dealer_label_5.grid(row=0, column=4, pady=20, padx=20)

# Labels for player cards
player_label_1 = tkinter.Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = tkinter.Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = tkinter.Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)

player_label_4 = tkinter.Label(player_frame, text='')
player_label_4.grid(row=1, column=3, pady=20, padx=20)

player_label_5 = tkinter.Label(player_frame, text='')
player_label_5.grid(row=1, column=4, pady=20, padx=20)

# menu buttons
start_button = tkinter.Button(root, text="START", command=game_start)
start_button.place(x=0, y=0, height=50, width=100)
endButton = tkinter.Button(root, text="END", command=game_end)
endButton.place(x=100, y=0, height=50, width=100)

# default state of buttons
stand["state"] = "disabled"
hit["state"] = "disabled"
fold["state"] = "disabled"
start_button["state"] = "normal"

root.mainloop()
