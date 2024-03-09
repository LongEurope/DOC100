#OOP true/false game
#It is possible to swap out the database with other stuff, and because it's OOP its possible, and if it was procedural it would've been a pain in the ass

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    added_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(added_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print('You\'ve completed the quiz')
print(f'Your final score is {quiz.score} out of {len(question_bank)}')