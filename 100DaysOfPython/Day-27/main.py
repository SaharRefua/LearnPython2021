from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am A Label" , font=("Arial", 24, "bold"))
my_label.pack()

# Entry
input = Entry(width=10)
input.pack()


# Bottom
def button_clicked():
    print("I got clicked")
    #my_label.config(text="Button was clicked")
    # Or use the next command :  my_label["text"] = "Button was clicked"
    user_input = input.get()
    my_label.config(text=user_input)

button = Button(text="Click Me", command=button_clicked)
button.pack()




window.mainloop()
