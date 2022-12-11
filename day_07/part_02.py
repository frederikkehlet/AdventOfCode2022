from treelib import Node, Tree
tree = Tree()
sums = {}

def sum_nodes(nid):      
    node = tree.get_node(nid)
    summation = 0

    if (len(tree.children(nid)) == 0):
        return node.data
    
    for child in tree.children(node.identifier):
        summation = summation + sum_nodes(child.identifier)
       
    sums[nid] = summation
    return summation

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()][1:]
    tree.create_node("/", "/", data=0)
    current_dir = "/"
    
    for line in lines:
        if line.split(' ')[0] == 'dir':        
            try:    
                tree.create_node(line.split(' ')[1], current_dir + line.split(' ')[1], parent=current_dir, data=0)
            except:
                continue
            
        elif line.split(' ')[1] == 'cd' and line.split(' ')[2] == '..':
            parent_node = tree.parent(current_dir)
            if (parent_node != None):
                current_dir = parent_node.identifier

        elif line.split(' ')[1] == 'cd' and line.split(' ')[2] != '..':
            current_dir = current_dir + line.split(' ')[2]

        elif line.split(' ')[0] != '$':
            try:
                tree.create_node(line.split(' ')[1], current_dir + line.split(' ')[1], parent=current_dir, data=int(line.split(' ')[0]))
            except:
                continue
            
    tree.show()
    sum_nodes("/")

    required = 30000000 - (70000000 - sums["/"])
    result = {k: v for k,v in sums.items() if v >= required}
    print(sorted(list(result.values()))[0])
   





    
    
    
        

    

