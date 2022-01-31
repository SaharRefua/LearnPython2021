from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_mark1.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps =0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def stat_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    # work_sec = 3
    # short_break_sec = 5
    # long_break_sec = 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        stat_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_mark1.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text="Timer", font=("Arial", 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", font=("Arial", 10, "bold"), bg="White", highlightthickness=0, command=stat_timer)
start_button.grid(column=1, row=4)

reset_button = Button(text="Reset", font=("Arial", 10, "bold"), bg="White", highlightthickness=0, command=reset_timer)
reset_button.grid(column=4, row=4)

check_mark1 = Label(font=("Arial", 25, "bold"), fg=GREEN, bg=YELLOW)
check_mark1.grid(column=2, row=5)

window.mainloop()
