import json
import random

# import rich

hits, mistakes = [], []


def read_json() -> dict:
    json_file = "/home/anderdam/DataEngineering/scripts/aws_trainning/questions.json"
    with open(json_file) as js:
        return json.load(js)


def initial_questions() -> dict:
    return read_json()


def reduced_questions(question_to_remove):
    original_questions = read_json()
    return original_questions.pop(question_to_remove[0])


def get_question(questions_to_choose_from) -> tuple:
    questions_list = questions_to_choose_from
    limit = len(questions_list)
    random_number = random.randint(1, limit)
    question_number = f"Question {random_number}"
    question = questions_list[question_number][0]
    right_answer = questions_list[question_number][1]
    checked = questions_list[question_number][2]  # Use the information or remove access
    return question_number, question, right_answer, checked


def score(hit, mistake):
    return f"""
    #########################################
    ### Score: Rights - {len(hit)} X Mistakes - {len(mistake)} ###
    #########################################

    """


def start(question_tuple):
    question_number, display_question, right_answer, checked = question_tuple

    limit = len(initial_questions())

    print(question_number, f"{limit}")
    print(display_question)
    print("")

    user_answer = input("Enter a option: ")
    print("\n")
    if user_answer == right_answer:
        hits.append(question_number)
        print("*** CORRECT ***")
        # Uncomment and utilize information if needed
        # if checked:
        #     print(f"Checked!")
    else:
        mistakes.append(question_number)
        print("!!! WRONG !!!")
        print(f"Correct answer was: {right_answer}")
        # Uncomment and utilize information if needed
        # if checked:
        #     print(f"Checked!")

    print(score(hits, mistakes))

    next_question = input("Continue to next question (yes/no)? ").lower()
    if next_question == "yes":
        limit -= 1
        question_to_remove = get_question(initial_questions())
        start(question_to_remove)
        # TODO Maybe add a stop condition based on limit or dictionary size
    else:
        print("### Fim de jogo ###\n")
        print(f"Resultado final:\n{score(hits, mistakes)}")


if __name__ == "__main__":
    start(get_question(initial_questions()))
