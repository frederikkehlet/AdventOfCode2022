with open('input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file.readlines()]
    edges = (len(lines) - 1 + len(lines[0]) - 1) * 2
    trees_visible = 0

    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            
            visible = True
            current_tree = int(lines[i][j])
            top_trees = []
            
            #top
            for k in range(i):
                top_trees.append(lines[k][j])

            #right
            right_trees = []
            for k in range(j + 1,len(lines)):
                right_trees.append(lines[i][k])

            #bottom
            bottom_trees = []
            for k in range(i + 1, len(lines)):
                bottom_trees.append(lines[k][j])

            #left
            left_trees = []
            for k in range(j):
                left_trees.append(lines[i][k])
            
            if(all(int(tree) < current_tree for tree in top_trees) or all(int(tree) < current_tree for tree in right_trees)
            or all(int(tree) < current_tree for tree in bottom_trees) or all(int(tree) < current_tree for tree in left_trees)):
                trees_visible = trees_visible + 1

    print(trees_visible + edges)