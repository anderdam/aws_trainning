import json
import random

hits, mistakes = [], []


def questions() -> dict:
    json_file = "questions.json"
    with open(json_file) as js:
        return json.load(js)


def get_question(question_dict) -> tuple:
    questions_list = question_dict
    limit = len(questions_list)
    while limit > 0:
        random_number = random.randint(1, limit)
        for key, value in questions_list.items():
            # Check if the key matches the random number
            if int(key.split()[1]) == random_number:
                # Print the key if found
                question_number = key
                question = value[0]
                right_answer = value[1]
                checked = True if value[2] == "Checked" else "False"

                return question_number, question, right_answer, checked


def is_checked(question):
    return True if question == "checked" else False


def score(hit, mistake):
    return f"""
    #########################################
    ### Score: Rights - {len(hit)} X Mistakes - {len(mistake)} ###
    #########################################
    
    """


def start():
    question_number = f"{get_question(questions())[0]} out of {len(questions())}"
    question = get_question(questions())[1]
    right_answer = get_question(questions())[2]
    checked = is_checked(get_question(questions())[3])

    print(question_number)
    print(question)
    print("")

    next_question = "yes"

    while next_question == "yes":
        user_answer = input("Enter a option: ")
        print("\n")
        if user_answer == right_answer:
            hits.append(question_number)
            print("\n*** CORRECT ***")
            print(f"### Checked? {checked} ###")
        else:
            mistakes.append(question_number)
            print("!!! WRONG !!!\n")
            print(f"Correct answer was: {right_answer}")
            print(f"Checked? {checked}\n")

        print(score(hits, mistakes))
        next_question = input("Continue to next question (yes/no)? ").lower()
        if next_question == "yes":
            start()
        else:
            break


if __name__ == "__main__":
    start()
