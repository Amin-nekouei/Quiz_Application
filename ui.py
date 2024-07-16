from tkinter import *  # Import all components from the tkinter module for GUI creation
from quiz_brain import QuizBrain  # Import the QuizBrain class that handles quiz logic

THEM_COLOR = "#B1DDC6"


class QuizInterface:
    """
           Initialize the QuizInterface class which sets up the GUI for the quiz.

           Args:
           quiz (QuizBrain): An instance of the QuizBrain class to manage quiz logic.
           """
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk() # Create the main application window
        self.window.config(bg=THEM_COLOR, pady=20, padx=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="",
            width=290,
            font=("arial", 18, "italic"))

        # Create a Canvas widget to display the quiz question
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)

        # Create a Label widget to display the score
        self.score_lable = Label(text="", bg=THEM_COLOR, font=("arial", 15, "bold"))
        self.score_lable.grid(row=0, column=1, sticky="E")

        # Load images for the true and false buttons
        self.true_img = PhotoImage(file="./images/right.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, command=self.right_answer)
        self.true_button.grid(row=3, column=0)
        self.false_img = PhotoImage(file="./images/wrong.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, command=self.wrong_answer)
        self.false_button.grid(row=3, column=1)
        self.update_question()  # Update the question display
        self.window.mainloop()  # Start the main event loop of the Tkinter application

    def update_question(self):
        """
        Update the question displayed on the canvas and the score label.
        Disable buttons if there are no more questions.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():

            self.score_lable.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f"          END\nYour total score is:\n            {self.quiz.score}")
            self.true_button.config(state="disable")
            self.false_button.config(state="disabled")
            self.score_lable.config(text="")
    def wrong_answer(self):
        """
        Handle the event when the false button is pressed.
        """
        is_right = self.quiz.scoring("False")
        self.feedback(is_right)
    def right_answer(self):
        """
        Handle the event when the true button is pressed.
        """
        is_right = self.quiz.scoring("True")
        self.feedback(is_right)

    def feedback(self,check):
        """
        Provide visual feedback on the canvas based on whether the answer was correct or not.

        Args:
        check (bool): True if the answer was correct, False otherwise.
        """
        if check:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.update_question)

