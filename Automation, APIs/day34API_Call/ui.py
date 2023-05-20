from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, q:QuizBrain):
        self.qb_current = q
        self.window = Tk()
        self.window.title("Qizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg = "white" )
        self.label = Label(text="Score: 0")
        self.label.grid(row = 0, column = 1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(150, 125, text= "q", font=("Arial", 20, "italic"), width=280)
        right_button = PhotoImage(file="images/true.png")
        wrong_button = PhotoImage(file="images/false.png")
        self.true_button = Button(image= right_button, highlightthickness= 0, command = self.true_click)
        self.false_button = Button(image= wrong_button, highlightthickness=0, command= self.false_click)
        self.true_button.grid(row = 2, column =0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.qb_current.still_has_questions():
            q_to_display = self.qb_current.next_question()
            self.canvas.itemconfig(self.canvas_text, text = q_to_display)
        else:
            self.canvas.itemconfig(self.canvas_text, text="youve reached the end of the quiz")
            self.true_button.config(state = "disabled")
            self.false_button.config(state="disabled")
    def true_click(self):
        result = self.qb_current.check_answer("true")
        self.label.config(text=f"score: {self.qb_current.score}")
        self.give_feedback(result)


    def false_click(self):
        result = self.qb_current.check_answer("false")
        self.label.config(text= f"score: {self.qb_current.score}")
        self.give_feedback(result)

    def give_feedback(self, result):
        if result:
            self.canvas.config( bg="green")
        else:
            self.canvas.config( bg="red")
        self.window.after(1000, self.get_next_question)


