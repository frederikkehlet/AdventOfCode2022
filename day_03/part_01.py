import string
alphabet = list(string.ascii_lowercase)
sum = 0

with open('input.txt', 'r') as file:
    rucksacks = [list(line.strip()) for line in file.readlines()]
    
    for items in rucksacks:
        intersections = list(set(items[:len(items)/2]) & set(items[len(items)/2:]))
        
        for intersection in intersections:
            if intersection in alphabet:
                sum = sum + alphabet.index(intersection) + 1
            else:
                sum = sum + alphabet.index(intersection.lower()) + 27
                
    print(sum)