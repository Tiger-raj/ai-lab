#solve suing UCS

import heapq

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        # initialize a node with the puzzle state, parent node, action, and path cost
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        if self.parent:
            self.path_cost += parent.path_cost

    def __lt__(self, node):
        # override less than operator for node comparison based on path cost
        return self.path_cost < node.path_cost

    def actions(self):
        # return a list of possible actions
        actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        return actions

    def result(self, action):
        # return a new node with the updated state after performing the action
        new_state = [x[:] for x in self.state]
        i, j = self.find_blank(new_state)
        if action == 'UP' and i > 0:
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif action == 'DOWN' and i < len(new_state) - 1:
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif action == 'LEFT' and j > 0:
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif action == 'RIGHT' and j < len(new_state[i]) - 1:
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        else:
            return None
        return Node(new_state, self, action, 1)

    def find_blank(self, state):
        # find the position of the blank space (0) in the puzzle
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    return i, j

    def goal_test(self, goal):
        # check if the current state matches the goal state
        return self.state == goal

    def solution(self):
        # return the sequence of actions to reach the current state from the start state
        path = []
        node = self
        while node:
            path.append(node)
            node = node.parent
        path.reverse()
        return path

def read_matrix():
    # read a 3x3 matrix from the user
    matrix = []
    for _ in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def ucs(start, goal):
    # perform uniform cost search from the start state to the goal state
    start = Node(start)
    queue = []
    heapq.heappush(queue, start)
    visited = set([str(start.state)])

    while queue:
        node = heapq.heappop(queue)
        if node.goal_test(goal):
            return node.solution()
        for action in node.actions():
            child = node.result(action)
            if child and str(child.state) not in visited:
                heapq.heappush(queue, child)
                visited.add(str(child.state))
    return None

def print_solution(solution):
    # print the solution path
    for node in solution:
        print("Action: ", node.action, ", Cost: ", node.path_cost)
        for row in node.state:
            print(row)
        print()

def main():
    # main function to read input and perform UCS
    print("Enter the start state matrix:")
    start = read_matrix()
    print("Enter the goal state matrix:")
    goal = read_matrix()
    solution = ucs(start, goal)
    print("The optimal sequence of moves is:")
    print_solution(solution)

if __name__ == "__main__":
    main()
