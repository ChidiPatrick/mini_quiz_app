class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Generate next question
    def next_question(self):
        current_question_obj = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question_obj["text"]} true/false\n")
        self.check_answer(answer.lower(), str(current_question_obj["answer"]).lower())
    # Check if we still have questions left in the question bank
    def still_have_questions(self):
        return self.question_number < len(self.question_list)
           
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("You got it wrong")
            print(f"Your current score is {self.score}/{self.question_number}")

        print(f"The correct answer is: {correct_answer}")




        