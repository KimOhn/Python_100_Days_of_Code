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

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    min = math.floor(count / 60)
    sec = count % 60
    if sec <10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text = f"{min}:{sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 100, pady = 100, bg = YELLOW)
canvas = Canvas(width = 200, height=224, highlightthickness= 0, bg= YELLOW)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 100, image = tomato)
timer_text = canvas.create_text(100, 102, text= "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column =1)

#Labels
label = Label(text="Timer", fg = GREEN, bg= YELLOW, font= (FONT_NAME, 20, "bold"))
label.grid(row = 0, column=1)
#Labels
checkmark = Label(text="✔", fg = GREEN, font= (FONT_NAME, 10, "bold"))
checkmark.grid(row = 2, column=1)

#Buttons
def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="LONG BREAK", fg = GREEN)
    elif reps % 2 == 1:
        count_down(WORK_MIN*60)
        label.config(text="WORK", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="SHORT BREAK", fg=PINK)


def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text = "Timer", fg = GREEN)
    reps = 0
#calls action() when pressed
start_button = Button(text="Start", command=start)
start_button.grid(row = 2, column=0)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(row = 2, column=2)




window.mainloop()