from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/english_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_text, text=current_card["English"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, fill="white", text="Russian/Belarusian")
    canvas.itemconfig(card_text, fill="white", text=f"{current_card['Russian']}/{current_card['Belarusian']}")


def known_card():
    to_learn.remove(current_card)

    # Save to csv
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# Canvas
canvas = Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
# canvas.itemconfig(timer_text, text="00:00")

canvas.grid(row=0, column=0, columnspan=2)

# Buttons

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_img, highlightthickness=0, command=known_card)
right_btn.grid(row=1, column=1)

next_card()


window.mainloop()

