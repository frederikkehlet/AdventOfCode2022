selection_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

strategy = { 
    'AX': 'draw',
    'AY': True,
    'AZ': False,
    'BX': False,
    'BY': 'draw',
    'BZ': True,
    'CX': True,
    'CY': False,
    'CZ': 'draw'   
}

selection_strategy = {
    'AX': 'Z',
    'AY': 'X',
    'AZ': 'Y',
    'BX': 'X',
    'BY': 'Y',
    'BZ': 'Z',
    'CX': 'Y',
    'CY': 'Z',
    'CZ': 'X'
}

with open('input.txt', 'r') as file:
    rounds = [line.strip().split(" ") for line in file.readlines()]
    score = 0

    for round in rounds: 
        selection = selection_strategy[str(round[0]+round[1])]   
        print(selection)
        if (strategy[str(round[0]+selection)] == 'draw'): #draw
            score = score + 3 + selection_score[selection]
        elif (strategy[str(round[0]+selection)]):
            score = score + 6 + selection_score[selection]
        else:
            score = score + selection_score[selection]

    print(score)