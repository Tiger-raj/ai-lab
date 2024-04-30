from collections import deque

class Node:
    def __init__(self, data, level, parent):
        self.data = data
        self.level = level
        self.parent = parent

    def generate_child(self):
        x, y = self.find(self.data, 0)
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, self)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j
        return None, None

class Puzzle:
    def __init__(self, size):
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        puz = []
        for i in range(0, self.n):
            temp = list(map(int, input().split(" ")))
            puz.append(temp)
        return puz

    def bfs(self, start, goal):
        start = Node(start, 0, None)
        queue = deque([start])
        visited = set([str(start.data)])

        while queue:
            state = queue.popleft()
            if state.data == goal:
                return state
            for child in state.generate_child():
                if str(child.data) not in visited:
                    queue.append(child)
                    visited.add(str(child.data))
        return None

    def print_path(self, state):
        if state.parent is not None:
            self.print_path(state.parent)
        for row in state.data:
            print(row)
        print()

    def process(self):
        print("Enter the start state matrix \n")
        start = self.accept()
        print("Enter the goal state matrix \n")
        goal = self.accept()

        goal_node = self.bfs(start, goal)
        if goal_node is None:
            print("No solution found.")
        else:
            print("Found solution in", goal_node.level, "steps.")
            self.print_path(goal_node)

puz = Puzzle(3)
puz.process()
