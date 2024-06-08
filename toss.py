import random

def toss(team1_choice, team2_choice):
    list1 = ['Head', 'Tail']
    return random.choice(list1)

result = toss('Head', 'Tail')
print(result)