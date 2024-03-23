#Source: https://stackoverflow.com/questions/76219308/i-get-an-type-error-but-o-cant-figure-out-why
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
reps = 0
timing = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomo():
    window.after_cancel(timing)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="TIMER")
    my_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    global reps
    reps += 1
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    work = WORK_MIN * 60
    if reps % 8 == 0:
        count_down(long)
        timer_text.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short)
        timer_text.config(text="Short Break")
    else:
        count_down(work)
        timer_text.config(text="WORK :)")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global time
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        timing = window.after(1000, count_down, count - 1)
    else:
        if reps % 8 != 0 and reps % 2 == 0:
            text = int(reps / 2) * "✔"
            my_label.config(text=text)
        start()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(103, 138, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_one = Button(text="Start", command=start)
button_one.grid(row=2, column=0)

button_two = Button(text="Reset", command=reset_pomo)
button_two.grid(row=2, column=2)

my_label = Label(bg=YELLOW, fg=GREEN)
my_label.grid(row=2, column=1)

timer_text = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_text.grid(row=0, column=1)

window.mainloop()