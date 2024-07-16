# Quiz Application

A Python-based quiz application with a graphical user interface (GUI) created using `tkinter`. This project includes functionalities for managing quiz questions, scoring, and providing feedback to the user.



## Project Overview

This project is a quiz application where users can answer a series of true/false questions. The application uses `tkinter` to create a user-friendly GUI. The questions and answers are fetched from an external API or a predefined data source. The `QuizBrain` class handles the logic for question management and scoring.

## Features

- **GUI Interface**: Interactive interface using `tkinter`.
- **Question Handling**: Fetch and display questions from a data source.
- **Scoring**: Track and display the user's score.
- **Feedback**: Provide visual feedback based on the user's answers.
- **End Screen**: Display the final score when the quiz ends.

## Code Overview

- **`main.py`**: The main script that initializes the quiz application.
- **`question_model.py`**: Defines the `Question` class to handle quiz questions and answers.
- **`quiz_brain.py`**: Implements the `QuizBrain` class to manage quiz logic, including question retrieval and scoring.
- **`ui.py`**: Manages the `QuizInterface` class for the graphical user interface.
- **`data.py`**: (Optional) Contains sample question data if not using an external API.

---

Happy quizzing!
