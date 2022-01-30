from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain
question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"]) #Question(item["text"], item["answer"])
    question_bank.append(question)
    #print(f"The question is : {question.text} and answer:  {question.answer}")

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your Final score was : {quiz.score}/{quiz.question_number}")
