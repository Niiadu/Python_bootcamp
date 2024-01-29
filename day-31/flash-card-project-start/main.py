from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# learn_words = pandas.DataFrame(data)
# learn_words.to_csv("words_to_learn.csv", index=False)
# new_learn_words = learn_words.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(translate_side, text=current_card["English"], fill="white")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(translate_side, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def known_words():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="./images/card_back.png")
front_card = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# back_image = canvas.create_image(400, 265,image=card_back)
card_image = canvas.create_image(400, 265, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)
language = canvas.create_text(400, 150, text="Title", font=("ariel", 40, "italic"))
translate_side = canvas.create_text(400, 263, text="word", font=("ariel", 60, "bold"))


wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=known_words)
right_button.grid(row=1, column=1)

next_word()




window.mainloop()
