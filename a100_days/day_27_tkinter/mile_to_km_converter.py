import tkinter


def start():

    def button_clicked():
        miles = float(input_miles.get())
        kms = round(miles * 1.609, 2)
        label_result.config(text=kms)

    window = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    # Input
    input_miles = tkinter.Entry(width=7)
    input_miles.grid(row=0, column=1)

    # Label Miles
    label_miles = tkinter.Label(text="Miles")
    label_miles.grid(row=0, column=2)

    # Label Equal
    label_equal = tkinter.Label(text="is equal to")
    label_equal.grid(row=1, column=0)

    # Label Result
    label_result = tkinter.Label(text="0")
    label_result.grid(row=1, column=1)

    # Label Km
    label_km = tkinter.Label(text="Km")
    label_km.grid(row=1, column=2)

    # Button
    button = tkinter.Button(text="Calculate", command=button_clicked)
    button.grid(row=2, column=1)



    window.mainloop()


if __name__ == '__main__':
    start()
