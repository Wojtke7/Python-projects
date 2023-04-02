class QuizBrain:
    question_number = 0
    question_list = []
    score = 0
    tries = 5

    def __init__(self, question_bank):
        self.question_list = question_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        correct_type = True
        while correct_type:
            answer1 = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            correct_type = self.check_answer(answer1, current_question)
            if self.tries == 0:
                print(f"End of the game, you lose")
            elif self.question_number == 12:
                print(f"Congratulations, you win!")

    def still_has_questions(self):
        if self.tries != 0:
            return self.question_number < len(self.question_list)
        else:
            return False

    def check_answer(self, answer, current_question):
        if answer == current_question.answer:
            self.score += 1
            print(f"Good choice, now your score is {self.score}")
            print(f"The correct answer was {current_question.answer}")
            print(f"You have {self.tries} tries left")
            return False
        elif answer == "True" or answer == "False":
            print(f"Bad choice, your score is {self.score}")
            self.tries -= 1
            print(f"The correct answer was {current_question.answer}")
            print(f"You have {self.tries} tries left")
            return False
        else:
            print(f"Unexpected answer, try again")
            return True
