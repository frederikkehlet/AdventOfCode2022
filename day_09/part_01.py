with open('input.txt', 'r') as file:
    motions = [line.strip().split(' ') for line in file.readlines()]

    head_pos = [0,0]
    tail_pos = [0,0]
    visited_pos = []

    for motion in motions:
        print(f'Motion: {motion}')

        if motion[0] == 'R':
            i = 0
            while i < int(motion[1]):
                head_pos[0] = head_pos[0] + 1
                
                if head_pos[0] - tail_pos[0] > 1 and head_pos[1] == tail_pos[1]:
                    tail_pos[0] = tail_pos[0] + 1
                elif head_pos[0] - tail_pos[0] > 1 and head_pos[1] != tail_pos[1]:
                    tail_pos[0] = tail_pos[0] + 1
                    tail_pos[1] = head_pos[1]

                i = i + 1
        elif motion[0] == 'L':
            i = 0
            while i < int(motion[1]):
                head_pos[0] = head_pos[0] - 1

                if head_pos[0] - tail_pos[0] > 1 and head_pos[1] == tail_pos[1]:
                    tail_pos[0] = tail_pos[0] - 1
                elif head_pos[0] - tail_pos[0] > 1 and head_pos[1] != tail_pos[1]:
                    tail_pos[1] = head_pos[1]
                    tail_pos[0] = tail_pos[0] - 1
                    
                i = i + 1
        elif motion[0] == 'U':
            i = 0
            while i < int(motion[1]):
                head_pos[1] = head_pos[1] + 1

                if head_pos[1] - tail_pos[1] > 1 and head_pos[0] == tail_pos[0]:
                    tail_pos[1] = tail_pos[1] + 1
                elif head_pos[1] - tail_pos[1] > 1 and head_pos[0] != tail_pos[0]:
                    tail_pos[0] = head_pos[0]
                    tail_pos[1] = tail_pos[1] + 1

                i = i + 1
        else: # down
            i = 0
            while i < int(motion[1]):

                head_pos[1] = head_pos[1] -1
                i = i + 1

        print(f'Head pos: {head_pos}')
        print(f'Tail pos: {tail_pos}')
        
        
        