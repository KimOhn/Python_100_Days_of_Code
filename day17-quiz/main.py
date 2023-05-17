from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(0,len(question_data)):
    q_text= question_data[i]["text"]
    q_answer = question_data[i]["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"your final score is {quiz_brain.score}/{quiz_brain.question_number}")