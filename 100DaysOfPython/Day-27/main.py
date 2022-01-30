from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #Space between the
# Label
my_label = Label(text="I Am A Label" , font=("Arial", 24, "bold"))
#my_label.pack()
my_label.grid(column=0, row=0)
# Entry
input = Entry(width=10)
#input.pack()
input.grid(column=3, row=2)

# Bottom
def button_clicked():
    print("I got clicked")
    #my_label.config(text="Button was clicked")
    # Or use the next command :  my_label["text"] = "Button was clicked"
    user_input = input.get()
    my_label.config(text=user_input)

button = Button(text="Click Me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)


button2 = Button(text="Click Me2")
button2.grid(column=2, row=0)
window.mainloop()
