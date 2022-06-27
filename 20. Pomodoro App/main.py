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
TEXT = ""
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # Aceasta functie opreste timpul care se scurge
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    global reps, TEXT
    reps = 0
    TEXT = ""
    my_label_check.config(text=TEXT)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global TEXT
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            TEXT += "✔"
            my_label_check.config(text=TEXT)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Promodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

my_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
my_label.grid(column=1, row=0)

start_button = Button(text="  Start  ", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="  Reset  ", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

my_label_check = Label(text=TEXT, fg=GREEN, font=(FONT_NAME, 18, "bold"), bg=YELLOW)
my_label_check.grid(column=1, row=3)

window.mainloop()
