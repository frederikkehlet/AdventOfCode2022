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

with open('input.txt', 'r') as file:
    rounds = [line.strip().split(" ") for line in file.readlines()]
    score = 0

    for round in rounds:    
        if (strategy[str(round[0]+round[1])] == 'draw'): #draw
            score = score + 3 + selection_score[round[1]]
        elif (strategy[str(round[0]+round[1])]):
            score = score + 6 + selection_score[round[1]]
        else:
            score = score + selection_score[round[1]]

    print(score)
