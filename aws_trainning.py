import json
import random

# import rich

hits, mistakes = [], []


def logo():
    print(
        """
        ╔═╗╦ ╦╔═╗  ╔═╗┬─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐┬─┐  ╔╦╗┬─┐┌─┐┬┌┐┌┌┐┌┬┌┐┌┌─┐
        ╠═╣║║║╚═╗  ╠═╝├┬┘├─┤│   │ ││ ││││├┤ ├┬┘   ║ ├┬┘├─┤││││││││││││ ┬
        ╩ ╩╚╩╝╚═╝  ╩  ┴└─┴ ┴└─┘ ┴ ┴└─┘┘└┘└─┘┴└─   ╩ ┴└─┴ ┴┴┘└┘┘└┘┴┘└┘└─┘
        \n
        P.S. "Choose two" questions need to be answered without \'/\', like AB, BC and so on...
        """
    )


def read_json() -> dict:
    json_file = "questions.json"
    with open(json_file) as js:
        return json.load(js)


def initial_questions() -> dict:
    return read_json()


def reduced_questions(question_to_remove) -> dict:
    new_questions = read_json()
    del new_questions[question_to_remove]
    return new_questions


def get_question(questions_to_choose_from) -> tuple:
    questions_list = questions_to_choose_from
    limit = len(questions_list)
    random_number = random.randint(1, limit)
    question_number = f"Question {random_number}"
    question = questions_list[question_number][0]
    right_answer = questions_list[question_number][1]
    check = questions_list[question_number][2]  # Use the information or remove access
    return question_number, question, right_answer, check


def score(hit, mistake):
    return f"""
    #########################################
    ### Score: Rights - {len(hit)} X Mistakes - {len(mistake)} ###
    #########################################
    """


def start(question_tuple, limit):
    question_number, display_question, right_answer, check = question_tuple

    limit = limit

    print(question_number, f"(Remainning: {limit})")
    print(display_question)
    print("")

    user_answer = input("Enter a option: ")
    print("\n")
    if user_answer.upper() == right_answer.upper():
        hits.append(question_number)
        print("*** CORRECT ***")
    else:
        mistakes.append(question_number)
        print("!!! WRONG !!!")
        print(f"Correct answer was: {right_answer}")
        print(check)

    print(score(hits, mistakes))

    next_question = input("Continue to next question ([Y]es/[N]o)? \n").lower()
    if next_question == "yes" or next_question == "y":
        limit -= 1
        start(get_question(reduced_questions(question_number)), limit=limit)
        # TODO Maybe add a stop condition based on limit or dictionary size
    else:
        print("### Fim de jogo ###\n")
        print(f"Resultado final:\n{score(hits, mistakes)}")


if __name__ == "__main__":
    logo()
    try:
        start(get_question(initial_questions()), limit=len(initial_questions()))
    except KeyboardInterrupt:
        print("\nThanks for your time and good luck in your certification :) ")
