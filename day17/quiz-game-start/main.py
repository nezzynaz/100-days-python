'''Main quiz game project.'''
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    QUESTION_TEXT = question["text"]
    QUESTION_ANSWER = question["answer"]

    # Instead of using variables here, you can directly call it. Like (question_data[0])
    new_question = Question(question_text=QUESTION_TEXT, answer=QUESTION_ANSWER)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
