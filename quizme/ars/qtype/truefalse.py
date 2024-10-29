"""Module for the TrueFalse quiz item class in the Adaptive Review System."""
from .question import Question

class TrueFalse(Question):
    """Class for a True/False quiz item."""
    def __init__(self, question, answer, explanation = ""):
        """Initialize a true/false quiz item.
            
        Args:
            question (str): The question to be displayed.
            answer (bool): The correct answer, either True or False.
            explanation (str, optional): Additional information to explain the correct answer.

        Raises:
            ValueError: If the answer is not a boolean.
        """ 
        super().__init__(question, answer)
        if not isinstance(answer, bool):
            raise ValueError("The answer must be a boolean (True or False)")
        self._explanation = explanation

    def ask(self) -> str:
        """Return the true/false question text."""
        super().ask()
        return self._question + " (True/False)"
    
    def check_answer(self, answer: str) -> bool:
        """Check if the provided answer is correct.
            
        Args:
            answer (str): The user's answer to the question.
            
        Returns:
            bool: True if the answer is correct, False otherwise.
            
        Raises:
            ValueError: If the answer is not 'True' or 'False'.
        """
        answer = (answer.strip()).lower()

        if answer == "true" or answer == "t":
            user_answer = True
        elif answer == "false" or answer == "f":
            user_answer = False
        else:
            raise ValueError("Answer must be 'True' or 'False'.")
        
        if user_answer == self._answer:
            return True
        else:
            return False
        
    def incorrect_feedback(self) -> str:
        """Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer, including the explanation if provided.
        """
        if self._explanation != "":
            return "Incorrect. " + self._explanation
        else:
            return "Incorrect. "

        

