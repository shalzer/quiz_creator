# Import the necessary modules for GUI (tkinter) and random selection
# Function to read and prepare quiz questions from a text file
    # Open the file and read everything inside
    # Create an empty list to store the processed questions
    # Go through each question block:
        # Skip it if it doesn't have enough lines (probably incomplete)
            # Try to pull out the question text, choices (A–D), and the correct answer
            # Store all of this in a dictionary and add it to the list
            # If something goes wrong, just skip that question
    # Send back the complete list of questions
# Create the main quiz app using a class
        # Set up the main window (title, size, background color)
        # Show a title and the current score
        # Create a label where the question text will go
        # Make four buttons for the answer choices (A to D)
        # Add a label to show feedback (right or wrong)
        # Add a button to go to the next question — it starts off disabled
        # Load the first question right away
    # Function to load and show a new question
            # If we’ve already gone through all the questions:
        # Otherwise, pick a random question that hasn’t been used yet
        # Show the question and its answer choices
        # Keep the next button disabled until an answer is selected
    # Function to check if the selected answer is correct
            # If it’s right, add 1 to the score and show a “correct” message
            # If it’s wrong, show the correct answer and a “wrong” message
        # Disable all the answer buttons so the user can’t change their answer
        # Update the score display
        # Enable the “Next Question” button so they can continue
# When the script is run directly:
    # Load questions from the text file
    # If no questions are found, print a warning
    # Otherwise, create the quiz window and start the app

import tkinter as tk
import random

def load_questions(file):
    with open(file, "r") as f:
        blocks = f.read().strip().split("\n-----------------\n")

    question = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 6: continue

        try:
            q = lines[0].split("Question: ")[1]
            a, b, c, d = (l.split(") ")[1] for l in lines[1:5])
            ans = lines[5].split("Answer: ")[1].strip()

            questions.append({"question": q, "choices": dict(zip("ABCD", [a, b, c, d])), "answer": ans})
