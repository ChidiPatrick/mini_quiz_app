from data import question_data
from quiz_brain import QuizBrain

class Question:
    def __init__(self,text, answer):
        self.text = text
        self.answer = answer

question_bank = []
question_number = 1

for i in question_data:
    question_bank.append({f"text":i["text"], "answer": i["answer"]})
    question_number += 1

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score} / {quiz.question_number}")
