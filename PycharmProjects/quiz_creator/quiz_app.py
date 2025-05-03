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


def load_questions(file_path):
    with open(file_path, "r") as file:
        blocks = file.read().strip().split("\n-----------------\n")

    questions = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 6:
            continue

        try:
            question_text = lines[0].split("Question: ")[1]
            choices = (line.split(") ")[1] for line in lines[1:5])
            correct_answer = lines[5].split("Answer: ")[1].strip()

            questions.append({
                "question": question_text,
                "choices": dict(zip("ABCD", choices)),
                "answer": correct_answer
            })
        except:
            continue

    return questions

class QuizApp:
    def __init__(self, master, question_data):
        self.master = master
        self.question_data = question_data.copy()
        self.score = 0
        self.total_questions = len(question_data)
        self.style = {"font": ("Roboto", 12, "bold"), "bg": "#0f172a", "fg": "white"}

        master.title("🎮 QUIZ APP ")
        master.geometry("600x550")
        master.configure(bg="#0f172a")

        tk.Label(master, text="⚔️ Test Your Skills!", font=("Roboto", 20, "bold"), bg="#0f172a", fg="#facc15", pady=10).pack()
        self.score_label = tk.Label(master, **self.style)
        self.score_label.pack()

        self.question_label = tk.Label(master, font=("Roboto", 14, "bold"), fg="#e0e0e0", bg="#0f172a", wraplength=550, pady=20)
        self.question_label.pack()

        self.answer_buttons = {
            option: tk.Button(master, width=50, bg="#1e293b", fg="white", activebackground="#f43f5e",
                         activeforeground="white", relief="groove", borderwidth=3, font=self.style["font"],
                         command=lambda option=option: self.check(option)) for option in "ABCD"
        }
        for button in self.answer_buttons.values(): button.pack(pady=6)

        self.result_label = tk.Label(master, font=("Roboto", 14, "bold"), bg="#0f172a", fg="white")
        self.result_label.pack(pady=20)

        self.next_button = tk.Button(master, text="➡️ Next Question", font=self.style["font"],
                                  bg="#3b82f6", fg="white", activebackground="#2563eb",
                                  state="disabled", command=self.next)
        self.next_button.pack(pady=10)
        self.next()

    def next(self):
        if not self.question_data:
            # If we’ve already gone through all the questions:
            self.question_label.config(text="🎉 Quiz Complete!")
            self.result_label.config(text=f"Final Score: {self.score} / {self.total_questions}")
            self.next_button.config(state="disabled")
            for button in self.answer_buttons.values(): button.config(state="disabled")
            return

        self.current_question = random.choice(self.question_data)
        self.question_data.remove(self.current_question)
        self.question_label.config(text=self.current_question["question"])

        for option_key, option_value in self.current_question["choices"].items():
            self.answer_buttons[option_key].config(text=f"{option_key}) {option_value}", state="normal")
        self.result_label.config(text="")

        self.next_button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")

    def check(self, pick):
        if pick == self.current_question["answer"]:
            self.score += 1
            self.result_label.config(text="✅ TAMA! Galing ah", fg="#10b981")
        else:
            # If it’s wrong, show the correct answer and a “wrong” message
            right = self.current_question["choices"][self.current_question["answer"]]
            self.result_label.config(text=f"❌ Mali! Ito tama oh: {self.current_question['answer']}) {right}", fg="#f43f5e")

        for button in self.answer_buttons.values(): button.config(state="disabled")
        self.score_label.config(text=f"Score: {self.score} / {self.total_questions}")
        self.next_button.config(state="normal")

if __name__ == "__main__":
    quiz = load_questions("quiz_data.txt")
    if not quiz:
        print("No questions found.")
    else:
        root = tk.Tk()
        QuizApp(root, quiz)
        root.mainloop()
