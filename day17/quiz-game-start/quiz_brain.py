'''Quiz Brain'''

class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        '''Checks to see if questions remain.'''
        return self.question_number < len(self.question_list)

# remember to import self into other methods in the class.

    def next_question(self):
        '''Prompts the user for each question and brings up the number by one.'''
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Question {self.question_number}: {current_question.text} (True/False):\n> ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        '''checks if the users input was correct.'''
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")