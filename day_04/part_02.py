with open('input.txt', 'r') as file:
    pairs = [line.strip().split(',') for line in file.readlines()]   
    overlaps = 0

    for pair in pairs:
        elf1 = [int(num) for num in pair[0].split('-')]
        elf2 = [int(num) for num in pair[1].split('-')]

        if ((elf1[0] >= elf2[0] and elf1[0] <= elf2[1]) or (elf1[1] >= elf2[0] and elf1[1] <= elf2[1])
        or (elf2[0] >= elf1[0] and elf2[0] <= elf1[1]) or (elf2[1]) >= elf1[0] and elf2[1] <= elf1[1]):
            overlaps = overlaps + 1

    print(overlaps)