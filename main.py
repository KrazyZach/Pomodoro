import tkinter as tk
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#config
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)
PHOTO = tk.PhotoImage(file="tomato.png")

#This is for the title 
title = tk.Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, highlightthickness=0, bg=YELLOW)

#Build the Tomato that hosts the timer
canva = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canva.create_image(100, 112, image=PHOTO)
timer_text = canva.create_text(100, 132, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))

reps = 0

def count_down(count):
    global x
    minutes = int(count / 60)
    seconds = int(count - (minutes * 60))
    if seconds <= 9:
        seconds = f"0{seconds}"

    canva.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        x = root.after(1000, count_down, count - 1)
    else:
        start_timer()

def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        title.config(text=f"Work", fg=GREEN)
        count_down(work_sec)
        reps += 1
    elif reps == 1 or reps == 3 or reps == 5:
        title.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        reps += 1
        check.config(text="✔" * (reps // 2))
    elif reps == 7:
        title.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps += 1
    else:
        end_timer()

def end_timer():
    global reps
    reps = 0
    title.config(text="Timer", fg=GREEN)
    check.config(text="")
    root.after_cancel(x)
    canva.itemconfig(timer_text, text="0:00")



#buttons 
start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
reset = tk.Button(text="Reset", highlightthickness=0, command=end_timer)

#Stage counter 
check = tk.Label(fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15))

#layout
title.grid(row=0, column=1)
canva.grid(row=1, column=1)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)
check.grid(row=3, column=1)

tk.mainloop()