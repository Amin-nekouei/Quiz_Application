import html


class QuizBrain:
    def __init__(self, question_list):
        """
        Initializes the QuizBrain with a list of questions.

        Args:
        question_list (list): A list of question objects where each object has 'text' and 'answer' attributes.
        """
        self.question_number = 0  # Keeps track of the current question number
        self.question_list = question_list  # List of all questions
        self.score = 0  # User's score initialized to zero
        self.current_question = None  # Holds the current question object

    def still_has_question(self):
        """
        Checks if there are more questions left in the list.

        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question from the list and increments the question number.

        Returns:
        str: A formatted string with the current question number and text.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # Unescape HTML entities in the question text
        question_text = html.unescape(self.current_question.text)
        # Format the question text with the current question number
        formatted_question = f"Q{self.question_number}: {question_text}"

        return formatted_question

    def scoring(self, answer):
        """
        Checks if the provided answer is correct and updates the score.

        Args:
        answer (str): The user's answer to the current question.

        Returns:
        bool: True if the answer is correct, False otherwise.
        """
        if answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False
