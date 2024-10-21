def question(question, correct_answer):
    answer = input(f"{question}\n")
    if answer == correct_answer:
        return 1
    else:
        return 0

def main():

    boolean = input("Do you want to play the quiz (Yes/No): ")
    questions = ["Onko tänään maanantai", "Onko kala hyönteinen?"]
    answers = ["Kyllä", "Ei"]
    sum = 0

    if boolean == "Yes":
        i = 0
        while boolean == "Yes":
            sum = sum + question(questions[i], answers[i])
            i = i+1
            if i == len(questions):
                boolean = "No"

    print("Final points:", sum)

main()
