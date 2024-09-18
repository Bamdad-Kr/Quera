import re
def hashtag_placement(answer, with_hashtag):
    left, right = with_hashtag.split('#')
    if left in answer or right in answer:
        return True
    else:
        return False

def solve(arr):
    eq, anwer_Of_eq = arr.split('=')
    first_variable, second_variable = eq.split('+')

    if "#" in anwer_Of_eq:
        answer = int(first_variable) + int(second_variable)
        answer = str(answer)
        if "#" in eq_answer:
            return f'{first_variable} + {second_variable} = {answer}'
        else:
            return '-1'

    if "#" in first_variable:
        answer = str(int(anwer_Of_eq) - int(second_variable))
        if hashtag_placement(answer, first_variable):
            return f'{answer} + {second_variable} = {anwer_Of_eq}'
        else:
            return '-1'

    if "#" in second_variable:
        answer = str(int(anwer_Of_eq) - int(first_variable))
        if hashtag_placement(answer, second_variable):
            return f'{first_variable} + {answer} = {anwer_Of_eq}'
        else:
            return '-1'
