from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dict_words = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("data/french_words.csv")
    dict_words = words.to_dict(orient="records")
else:
    data_words = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_words)
    canvas.itemconfig(french_word, text=current_card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(front_card, image=front_of_card)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(front_card, image=back_of_card)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(french_word, text=current_card["English"], fill="white")

def known_words():
    dict_words.remove(current_card)
    data = pandas.DataFrame(dict_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy")
front_of_card = PhotoImage(file="images/card_front.png")
back_of_card = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card = canvas.create_image(400, 263, image=front_of_card)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
french_word = canvas.create_text(400, 263, text="trouve", font=("ariel", 60, "bold"), fill="black")



right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=known_words)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)

next_word()


window.mainloop()
