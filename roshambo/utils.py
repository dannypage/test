import random


def game(choice):
    options = ['rock','paper','scissors']
    server_throw = random.sample(options,1)[0]

    result = options.index(server_throw) - options.index(choice)

    input = "You picked {}, while Server picked {}. ".format(choice, server_throw)
    response = "Strange result."
    if result == 0:
        response = "We Tied."
    if (result == -2) or (result == 1):
        response = "Server Wins."
    if (result == 2) or (result == -1):
        response = "You Win."
    return input + response