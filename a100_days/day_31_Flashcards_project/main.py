from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


def start():
    window = Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    # Images
    card_front_img = PhotoImage(file="./images/card_front.png")
    card_back_img = PhotoImage(file="./images/card_back.png")
    wrong_img = PhotoImage(file="./images/wrong.png")
    right_img = PhotoImage(file="./images/right.png")

    # Canvas
    canvas = Canvas(width=800, height=526, highlightthickness=0)
    canvas.create_image(400, 263, image=card_front_img)
    title_text = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT_NAME, 40, "italic"))
    word_text = canvas.create_text(400, 263, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))
    # canvas.itemconfig(timer_text, text="00:00")

    canvas.grid(row=0, column=0, columnspan=2)

    # Buttons

    wrong_btn = Button(image=wrong_img, highlightthickness=0)
    wrong_btn.grid(row=1, column=0)

    right_btn = Button(image=right_img, highlightthickness=0)
    right_btn.grid(row=1, column=1)




    window.mainloop()


if __name__ == '__main__':
    start()
