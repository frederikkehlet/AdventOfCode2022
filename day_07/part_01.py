import sys
sys.setrecursionlimit(100000)

lines = []
sums = {}

def solve(dir_name):
    sum = 0

    cmd = f'$ cd {dir_name}'

    if cmd in lines:
        start = lines.index(cmd) + 1
        i = start + 1
        line_is_not_command = True
        while line_is_not_command and i < len(lines):
            if ('$' in lines[i]):
                line_is_not_command = False
            else:
                i = i + 1
        items = lines[start+1:i]

        for item in items:
            if 'dir' in item:
                sum = sum + solve(item.split(' ')[1])
            else:
                sum = sum + int(item.split(' ')[0])

        sums[dir_name] = sum
        return sum

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    
    solve('/')
    print(sum(filter(lambda val: val < 100000, sums.values())))

    

