import random
import tkinter
from PIL import Image, ImageTk

# initializing variables
deck = []
player = []
dealer = []
dealer_card_slots = 0
player_card_slots = 0


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
    double["state"] = "normal"
    fold["state"] = "normal"
    start_button["state"] = "disabled"
    start()


# game end function
def game_end():
    # disables buttons
    stand["state"] = "disabled"
    hit["state"] = "disabled"
    double["state"] = "disabled"
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
    # deals 2 cards each to player and dealer
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()


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
            player.append(dealer_card)

            global dealer_image_1, dealer_image_2, dealer_image_3, dealer_image_4, dealer_image_5

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
                fold["state"] = "disabled"
                hit["state"] = "disabled"
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


# reset function
def reset():
    global player, dealer, player_card_slots, dealer_card_slots
    # reset all settings back to default
    refill_deck()
    player_card_slots = 0
    dealer_card_slots = 0
    root.title(f'Blackjack')
    player = []
    dealer = []


# resizing the card images
def resize_cards(card):
    card_image = Image.open(card)

    # resizing image
    card_image_resize = card_image.resize((113, 164))
    global card_img
    card_img = ImageTk.PhotoImage(card_image_resize)
    return card_img


def die():
    # reset and deal new hands
    reset()
    deal_player_card()
    deal_dealer_card()
    deal_player_card()
    deal_dealer_card()


# def calculate_player_hand():
#     total = 0
#     face = ["J", "Q", "K"]
#     for card in player:
#         if card in range(1, 11):
#             total += card
#         elif card in face:
#             total += 10
#         elif card == "A":
#             total += 11
#     if total == 21:
#         print("Blackjack! You win!")
#         print(f'Your total: {total}')
#         reset()
#     elif total > 21:
#         print("Bust! You lose!")
#         print(f'Your total: {total}')
#         reset()


# def calculate_dealer_hand():
#     total = 0
#     face = ["J", "Q", "K"]
#     for card in dealer:
#         if card in range(1, 11):
#             total += card
#         elif card in face:
#             total += 10
#         elif card == "A":
#             total += 11
#     if total == 21:
#         print("Dealer Blackjack! You lose")
#         print(f'Dealer total: {total}')
#         reset()
#     elif total > 21:
#         print("Dealer Bust! You win!")
#         print(f'Dealer total: {total}')
#         reset()


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
buttonFrame.columnconfigure(3, weight=1)

# play buttons
stand = tkinter.Button(buttonFrame, bg="#852928", fg='white',
                       text='Stand', font=('Arial', 16), command=deal_dealer_card)
stand.grid(row=0, column=0, sticky=tkinter.W + tkinter.E)
hit = tkinter.Button(buttonFrame, bg="black", fg='white',
                     text='Hit', font=('Arial', 16), command=deal_player_card)
hit.grid(row=0, column=1, sticky=tkinter.W + tkinter.E)
double = tkinter.Button(buttonFrame, bg="#852928", fg='white',
                        text='Double', font=('Arial', 16))
double.grid(row=0, column=2, sticky=tkinter.W + tkinter.E)
fold = tkinter.Button(buttonFrame, bg="black", fg='white',
                      text='Fold', font=('Arial', 16), command=die)
fold.grid(row=0, column=3, sticky=tkinter.W + tkinter.E)
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
double["state"] = "disabled"
fold["state"] = "disabled"
start_button["state"] = "normal"

root.mainloop()
