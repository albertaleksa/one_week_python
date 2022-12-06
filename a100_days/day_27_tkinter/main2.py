import tkinter


def button_clicked():
    input_text = input.get()
    my_label.config(text=input_text)


window = tkinter.Tk()
window.title("GIU Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.grid(row=0, column=0)
my_label.config(padx=30, pady=30)

# Button
my_button = tkinter.Button(text="Click on me", command=button_clicked)
my_button.grid(row=1, column=1)

# Entry
input = tkinter.Entry(width=10)
input.grid(row=2, column=3)

# Button2
my_button2 = tkinter.Button(text="New Button", command=button_clicked)
my_button2.grid(row=0, column=2)

window.mainloop()
