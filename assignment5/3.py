# determine the optimal strategy using minimax
class Node:
    # initialize node with value and children
    def __init__(self, value):
        self.value = value
        self.children = []
 
def minimax(node, depth, maximizing_player):
    # base case: if depth is 0 or node has no children
    if depth == 0 or len(node.children) == 0:
        return node.value
    
    if maximizing_player:
        value = float('-inf')
        # iterate over each child node
        for child in node.children:
            # recursive call to minimax function
            value = max(value, minimax(child, depth - 1, False))
        return value
    else:
        value = float('inf')
        # iterate over each child node
        for child in node.children:
            # recursive call to minimax function
            value = min(value, minimax(child, depth - 1, True))
        return value
 
# example game tree
root = Node(None)
node1 = Node(None)
node2 = Node(None)
node3 = Node(None)
node4 = Node(None)
node5 = Node(None)
 
root.children = [node1, node2]
node1.children = [node3, node4]
node2.children = [node5]
 
# leaf nodes with payoff values
node3.value = 3
node4.value = 6
node5.value = 2
 
# determine the optimal strategy using minimax
optimal_value = minimax(root, 2, True)
print("optimal value:", optimal_value)
