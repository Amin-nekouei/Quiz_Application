class Question:
    def __init__(self, text, answer):
        """
                Initializes a new Question object with the given text and answer.

                Args:
                text (str): The text of the question to be asked.
                answer (str): The correct answer to the question.
                """
        self.text = text  # Stores the question text
        self.answer = answer  # Stores the correct answer to the question
