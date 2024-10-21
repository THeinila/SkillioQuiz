def question(question, correct_answer):
    answer = input(question)
    if answer == correct_answer:
        return 1
    else:
        return 0

def main():

    boolean = input("Do you want to play the quiz (Yes/No): ")
    questions = []
    answers = []

    if boolean == "Yes":
        i = 0
        sum = 0
        while boolean == "Yes":
            sum = sum + question(questions[i], answers[i])
        if i == len(questions):
            boolean = "No"

    print("Final points: ", sum)

main()
