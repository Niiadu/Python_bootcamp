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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 1 * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN
    reps += 1
    if reps == 1 or reps == 3 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 45), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)




window.mainloop()
