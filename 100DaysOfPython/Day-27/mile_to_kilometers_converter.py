from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(column=3, row=1)

miles_label = Label(text="Km", font=("Arial", 14, "bold"))
miles_label.grid(column=3, row=2)


input = Entry(width=10)
input.grid(column=1, row=1)


my_label = Label(text="is equal to", font=("Arial", 14, "bold"))
my_label.grid(column=0, row=2)

result_label = Label(text="0", font=("Arial", 14))
result_label.grid(column=1, row=2)

def button_clicked():
    mile = float(input.get())
    km = round(mile * 1.609344)
    result_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
