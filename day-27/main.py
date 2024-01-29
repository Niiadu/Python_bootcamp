import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="My name is Jonas", font=("courier", 16))
# my_label.pack()
my_label.grid(column=0, row=0)

# my_label["text"] = "Majorie is my name"

def button_clicked():
    my_label.config(text=input.get())


# Button
button = tkinter.Button(text="Submit", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=3, row=2)


window.mainloop()