"""Module for the ShortAnswer quiz item class in the Adaptive Review System."""
import re
from .question import Question

class ShortAnswer(Question):
    """A quiz item representing a short answer question."""
    def __init__(self, question, answer, case_sensitive = False):
        """Initialize a short answer quiz item.

            Args:
                question (str): The question prompt.
                answer (str): The correct answer.
                case_sensitive (bool, optional): Whether the answer comparison should be case-sensitive. 
                                                Defaults to False.
            """
        super().__init__(question, answer)
        self._case_sensitive = case_sensitive
    
    def ask(self) -> str:
        """Return the true/false question text."""
        super().ask()
        return self._question + " (Short Answer)"
    
    def _normalize(self, text):
        """Normalize the text for comparison.

        Args:
            text (str): The text to normalize.

        Returns:
            str: The normalized text.
        """
        text = text.strip()
        if self._case_sensitive == False:
            text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def check_answer(self, answer):
        """Check if the provided answer is correct.

        Args:
            answer (str): The provided answer.

        Returns:
            bool: True if the provided answer is correct, False otherwise.
        """
        answer = self._normalize(answer)
        self._answer = self._normalize(self._answer)
        if answer == self._answer:
            return True
        else:
            return False
    
    def incorrect_feedback(self):
        """Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer.
        """
        return f"Incorrect. The correct answer is: {self._answer}"
    




