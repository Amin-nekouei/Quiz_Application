# Import necessary modules and classes
from question_model import Question  # Import the Question class to create question objects
from data import question_data  # Import the question data (e.g., a list of questions and answers)
from quiz_brain import QuizBrain  # Import the QuizBrain class to handle quiz logic
from ui import QuizInterface  # Import the QuizInterface class to create the quiz UI

# Initialize an empty list to hold Question objects
question_bank = []

# Loop through each item in the question_data list
for item in question_data:
    question = Question(item["question"],item["correct_answer"])
    question_bank.append(question)

# Create an instance of QuizBrain with the list of Question objects
quiz = QuizBrain(question_bank)

# Create the user interface for the quiz using the QuizInterface class
# Pass the QuizBrain instance to the QuizInterface so that it can interact with the quiz logic
quiz_ui = QuizInterface(quiz)








