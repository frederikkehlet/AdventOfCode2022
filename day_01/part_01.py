with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    indices = [ix for ix, line in enumerate(lines) if line == '']
    indices.insert(0,0)
    elves = [lines[i:j] for i,j in zip(indices, indices[1:]+[None])]

    for elf in elves:        
        cals = [int(cal) for cal in elf if cal != '']
        elves[elves.index(elf)] = sum(cals)

    print(max(elves))  