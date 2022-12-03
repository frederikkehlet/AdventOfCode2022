import string
alphabet = list(string.ascii_lowercase)
sum = 0

with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]
    groups = [lines[i * 3:(i + 1) * 3] for i in range((len(lines) + 3 - 1) // 3)]

    for rucksacks in groups:
        intersections = list(set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))
        
        for intersection in intersections:
            if intersection in alphabet:
                sum = sum + alphabet.index(intersection) + 1
            else:
                sum = sum + alphabet.index(intersection.lower()) + 27

    print(sum)