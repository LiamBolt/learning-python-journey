"""
A Spanish-English flashcard application built with tkinter.
This program helps users learn Spanish vocabulary through interactive
flashcards that flip between Spanish and English translations.
"""

from tkinter import Tk, Canvas, Button, PhotoImage
import pandas
import random

# Constants and global variables
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Load word data from CSV
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    """
    Display the next random flashcard in Spanish.
    Resets the flip timer and updates the card's front face with Spanish text.
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) > 0:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="Spanish", fill="black")
        canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black"
                          )
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """
    Flip the flashcard to show the English translation.
    Updates the card's back face with English text and white color.
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """
    Handle when user marks a card as known.
    Removes the current card from the learning list and saves progress.
    If all cards are learned, displays completion message and disables buttons.
    """
    global to_learn
    to_learn.remove(current_card)

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Completed!", fill="black")
        canvas.itemconfig(card_word, text="You've learned all the cards!",
                          fill="black")
        unknown_button.config(state="disabled")
        known_button.config(state="disabled")
    else:
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()


# Set up the main window
window = Tk()
window.title("Spanish-English Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Initialize flip timer
flip_timer = window.after(3000, func=flip_card)

# Create and configure the canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic")
                                )
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create and configure the buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,
                        command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,
                      command=is_known)
known_button.grid(row=1, column=1)

# Start the application with the first card
next_card()

# Start the main event loop
window.mainloop()
