class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?")
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)
    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("that's wrong")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

