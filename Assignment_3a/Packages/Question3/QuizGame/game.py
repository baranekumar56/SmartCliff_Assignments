
from questions import questions
import random


def conduct_quiz():
    score = 0
    questionss = list(questions.items())

    for i in range(0, len(questions)):

        question = questionss[random.randint(0, len(questions)-1)]

        print(question[0])
        answer = input()
        if answer == question[1]:
            score += 1

    return score
