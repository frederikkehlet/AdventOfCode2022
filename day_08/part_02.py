with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]
    edges = (len(lines) - 1 + len(lines[0]) - 1) * 2
    trees_visible = 0
    scores = []

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            
            visible = True
            current_tree = int(lines[i][j])
            top_trees = []
            trees = []
            print('Current tree: ' + str(current_tree))

            #top
            for k in range(i):
                top_trees.append(int(lines[k][j]))

            top_trees = list(reversed(top_trees))
            trees.append(top_trees)

            #right
            right_trees = []
            for k in range(j + 1,len(lines)):
                right_trees.append(int(lines[i][k]))

            trees.append(right_trees)

            #bottom
            bottom_trees = []
            for k in range(i + 1, len(lines)):
                bottom_trees.append(int(lines[k][j]))

            trees.append(bottom_trees)

            #left
            left_trees = []
            for k in range(j):
                left_trees.append(int(lines[i][k]))

            left_trees = list(reversed(left_trees))
            trees.append(left_trees)

            print(trees)
            scores = []
            
            for tree_line in trees:
                score = 0
                for i in range(len(tree_line)):
                    print(tree_line[i])
                    if tree_line[i] >= current_tree:
                        score = i + 1
                        break





            