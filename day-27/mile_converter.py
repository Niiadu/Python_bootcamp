from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=10)


def calculate():
    miles = float(entry.get())
    km_num = round(miles * 1.609344, 2)
    third_label.config(text=km_num)


entry = Entry(width=10)
entry.grid(column=1, row=0)

first_label = Label(text="Miles", font=("courier", 16))
first_label.grid(column=2, row=0)

second_label = Label(text="is equal to", font=("courier", 16))
second_label.grid(column=0, row=1)

third_label = Label(text=0, font=("courier", 16))
third_label.grid(column=1, row=1)

forth_entry = Label(text="Km", font=("courier", 16))
forth_entry.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()