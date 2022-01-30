from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)


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
    user_input = float(input.get())
    result = user_input*1.609344
    result_label.config(text=int(result))


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
