class Node:
    # constructor for the Node class
    def __init__(self, name, type, cost):
        self.name = name  # name of the node
        self.type = type  # type of the node (AND/OR)
        self.cost = cost  # cost of the node
        self.children = []  # list of children nodes

    # method to add a child node
    def add_child(self, node):
        self.children.append(node)

# AO* search algorithm
def AO_star(root, path=''):
    path += root.name  # add the name of the current node to the path
    if not root.children:  # if the node is a leaf
        return root.cost, path

    if root.type == 'AND':
        # calculate the cost and path for each child node
        costs_paths = [AO_star(child, path + ' -> ') for child in root.children]
        # calculate the total cost
        total_cost = root.cost + sum(cost for cost, _ in costs_paths)
        # concatenate the paths
        total_path = ' AND '.join(path for _, path in costs_paths)
        return total_cost, path + ' -> (' + total_path + ')'

    if root.type == 'OR':
        # calculate the cost and path for each child node
        costs_paths = [AO_star(child, path + ' -> ') for child in root.children]
        # find the child node with the minimum cost
        min_cost, min_path = min(costs_paths, key=lambda x: x[0])
        return root.cost + min_cost, path + ' -> ' + min_path

# create nodes
root = Node('Root', 'OR', 2)
node_A = Node('A', 'AND', 5)
node_B = Node('B', 'AND', 3)
node_C = Node('C', 'OR', 2)
node_D = Node('D', 'OR', 4)

# add children to the nodes
root.add_child(node_A)
root.add_child(node_B)
node_A.add_child(node_C)
node_A.add_child(node_D)

# run AO* search algorithm
cost, path = AO_star(root)
print(f'Cost: {cost}, Path: {path}')
