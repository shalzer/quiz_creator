#Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer.
#Write the collected data to a text file. Ask another question until the user chose to exit.

#set the file name to save the questions
#start an infinite loop that allows user to add questions
#ask user to input a new quiz question
#collect the question and choices from the user
#ask user to enter first, second, third, and fourth choice
#prompt user for the correct answer

#open the file in append mode to store question and choices
#write the question and choices to the file
#add a divider to separate questions

#ask user if they want to add another question
#if they answer "yes", tell the user that the quiz is saved
#else, break the loop
#exit loop

filename = "quiz_data.txt"

while True:
    print("\n Welcome to Quiz Creator !")

    question = input("Question: ")
    choice_a = input("A.) ")
    choice_b = input("B.) ")
    choice_c = input("C.) ")
    choice_d = input("D.) ")
    correct_answer = input("Correct answer: (A/B/C/D): ").upper()

    with open(filename, "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"A.) {choice_a}\n")
        file.write(f"B.) {choice_b}\n")
        file.write(f"C.) {choice_c}\n")
        file.write(f"D.) {choice_d}\n")
        file.write(f"Answer: {correct_answer} \n")
        file.write("\n-----------------\n")
    again = input("\nDo you want to add another question? (yes/no): ")
    if again.lower() != "yes":
        print("Quiz saved!")
        break