import json
import random

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
    json_file = "/home/anderdam/DataEngineering/scripts/aws_trainning/questions.json"
    with open(json_file) as js:
        return json.load(js)


def shuffled_questions():
    questions = list(
        read_json().items()
    )  # Convert dict to list of (question_number, question_data) tuples
    random.shuffle(questions)  # Shuffle the list in-place
    return questions


def score(hit, mistake):
    return f"""
    #########################################
                     Score                    
                Hits {len(hit)} X {len(mistake)} Mistakes          
    #########################################
    """


def start(question_list):
    limit = len(question_list) - 1
    for question_item in question_list:
        question_number = question_item[0]
        question = question_item[1][0]
        right_answer = question_item[1][1]
        link = question_item[1][2]

        print(question_number, f"(Remainning: {limit})")
        print(question)
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
            print(link)

        print(score(hits, mistakes))

        next_question = input("Continue to next question ([Y]es/[N]o)? ").lower()
        print("")
        if next_question == "yes" or next_question == "y":
            limit -= 1
            continue
        # TODO Maybe add a stop condition based on limit or dictionary size
        else:
            break

    print("### Fim de jogo ###\n")
    print(f"Resultado final:\n{score(hits, mistakes)}")


if __name__ == "__main__":
    logo()
    try:
        start(shuffled_questions())
    except KeyboardInterrupt:
        print("\nThanks for your time and good luck in your certification :) ")
