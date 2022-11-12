from a100_days.day_17_quiz_game_start.question_model import Question
from a100_days.day_17_quiz_game_start.data import question_data
from a100_days.day_17_quiz_game_start.quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
