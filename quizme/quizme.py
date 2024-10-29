"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""
from pathlib import Path
from typing import List, Dict, Any
import json
import argparse
from ars.arcontroller import ARController

def load_questions(file_path: Path) -> List[Dict[str, Any]]:
    """
    Load questions from a JSON file.

    Args:
        file_path (Path): Path to the JSON file containing quiz questions.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a quiz question.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"ERROR: '{file_path}' was not found.")
        raise
    except json.JSONDecodeError:
        print("JSON ERROR")
        raise

def run_quiz(name: str, questions: List[Dict[str, Any]]) -> None:
    """
    Run the adaptive quiz session.

    Args:
        name (str): The name of the quiz taker.
        questions (List[Dict[str, Any]]): A list of dictionaries containing question data.
    """
    print(f"Welcome to QuizMe {name}!")
    controller = ARController(questions)
    controller.start()

def main() -> None:
    """
    Main function to set up and run the QuizMe CLI application.
    """
    parser = argparse.ArgumentParser(description="Runs QuizMe CLI application with given questions")
    parser.add_argument("name", help="User's name")
    parser.add_argument("--questions", required=True, help="File path to JSON file containing questions")
    args = parser.parse_args()
    try:
        questions = load_questions(Path(args.questions))
        run_quiz(args.name, questions)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"ERROR: {e}")
        print(f"Error name: {type(e).__name__}")


if __name__ == "__main__":
    main()
