from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
show_answer = None
current_test = {}
#READ DATA from CSV -----#
try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_df = pandas.read_csv('data/french_words.csv')
    df_dict = original_df.to_dict(orient="records")
else:
    df_dict = df.to_dict(orient="records")




def is_known():
    df_dict.remove(current_test)
    words_to_learn = pandas.DataFrame(df_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    french_test()


# Random choice ---#
def french_test():
    global show_answer
    global current_test

    current_test = random.choice(df_dict)
    french_word_test = current_test["French"]
    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(card_language, text="French")
    canvas.itemconfig(card_word, text=french_word_test)
    show_answer = window.after(3000, display_back)


# Show English ---#
def display_back():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_language, text="English")
    canvas.itemconfig(card_word, text=current_test["English"])
    window.after_cancel(show_answer)

#CREATE UI -------------------------------#
window = Tk()
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

canvas = Canvas(width = 800, height= 526, highlightthickness= 0, bg= BACKGROUND_COLOR)
card_back = PhotoImage(file = "images/card_back.png")
card_front = PhotoImage(file = "images/card_front.png")
right_button = PhotoImage(file = "images/right.png")
wrong_button = PhotoImage(file = "images/wrong.png")

card = canvas.create_image(400, 250, image = card_front)
canvas.grid(row = 0, column =0, columnspan=2)

def right():
    pass
def wrong():
    pass
card_language = canvas.create_text(400, 150, text="",  font= ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="",  font= ("Ariel", 60, "bold"))
#calls action() when pressed
right_button_actual = Button(image= right_button, highlightthickness=0, command = is_known)
right_button_actual.grid(row =1, column=0)

wrong_button_actual = Button(image= wrong_button, highlightthickness= 0, command = french_test)
wrong_button_actual.grid(row =1, column=1)

french_test()
window.mainloop()



