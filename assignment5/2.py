class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
 
def minimax(node, depth, maximizing_player):
    if depth == 0 or len(node.children) == 0:
        return node.value
    
    if maximizing_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, minimax(child, depth - 1, True))
        return value
 
# Example game tree
root = Node(None)
node1 = Node(None)
node2 = Node(None)
node3 = Node(None)
node4 = Node(None)
node5 = Node(None)
 
root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5]
 
# Leaf nodes with payoff values
node3.value = 3
node4.value = 6
node5.value = 2
 
# Determine the optimal strategy using minimax
optimal_value = minimax(root, 2, True)
print("Optimal value:", optimal_value)
