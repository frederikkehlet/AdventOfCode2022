stacks = [
    ['N','D','M','Q','B','P','Z'],
    ['C','L','Z','Q','M','D','H','V'],
    ['Q','H','R','D','V','F','Z','G'],
    ['H','G','D','F','N'],
    ['N','F','Q'],
    ['D','Q','V','Z','F','B','T'],
    ['Q','M','T','Z','D','V','S','H'],
    ['M','G','F','P','N','Q'],
    ['B','W','R','M'] 
]

with open('input.txt', 'r') as file:
    instructions = [line.strip() for line in file.readlines()]
    
    for instruction in instructions:
        parts = instruction.split(' ')
        if int(parts[1]) == 1:
            temp = stacks[int(parts[3])-1].pop()
            stacks[int(parts[5])-1].append(temp)
        else:
            list_reversed = list(stacks[int(parts[3])-1][-int(parts[1]):])
            for num in list_reversed:
                stacks[int(parts[5])-1].append(num)
                stacks[int(parts[3])-1].pop()

    print(''.join([stack[-1] for stack in stacks]))