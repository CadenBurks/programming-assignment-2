"""Core module for running the Adaptive Review System (ARS) session."""
from .boxmanager import BoxManager
from .qtype.shortanswer import ShortAnswer
from .qtype.truefalse import TrueFalse

class ARController():
    """Main controller for running an adaptive review session."""
    def __init__(self, question_data):
        """Initialize the Adaptive Review Controller.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        self._box_manager = BoxManager()
        self._initialize_questions(question_data)
    
    def _initialize_questions(self, question_data):
        """Initialize questions and place them in the Unasked Questions box.

        Args:
            question_data (List[Dict[str, Any]]): A list of dictionaries containing question data.
        """
        for dictionary in question_data:
            try:
                if dictionary["type"] == "shortanswer":
                    instance = ShortAnswer(dictionary["question"], dictionary["correct_answer"])
                    self._box_manager.add_new_question(instance)
                elif dictionary["type"] == "truefalse":
                    instance = TrueFalse(dictionary["question"], dictionary["correct_answer"], dictionary["explanation"])
                    self._box_manager.add_new_question(instance)
                else:
                    print("Unsupported question type: invalid. Skipping this question.")
            except KeyError as e:
                print(f"Missing required field for question: {e}. Skipping this question.")
            
    
    def start(self) -> None:
        """Run the interactive adaptive review session."""
        print("Type 'q' at any time to quit the session.")
        while True:
            q = self._box_manager.get_next_question()
            if not q:
                print("All questions have been reviewed. Session complete!")
                break
            print(q.ask())
            user_answer = input("Answer: ")
            if user_answer == "q":
                break
            if isinstance(q, TrueFalse):
                try:
                    if q.check_answer(user_answer):
                        print("Correct!")
                        self._box_manager.move_question(q, True)
                    else:
                        print(q.incorrect_feedback())
                        self._box_manager.move_question(q, False)
                except ValueError:
                    print("Invalid input: Answer must be 'True' or 'False'.")
            else:
                if q.check_answer(user_answer):
                        print("Correct!")
                        self._box_manager.move_question(q, True)
                else:
                    print(q.incorrect_feedback())
                    self._box_manager.move_question(q, False)
        print("Thank you, goodbye!")            




