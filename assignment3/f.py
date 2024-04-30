class Node:
    # initialization method for Node class
    def __init__(self, data, level):
        self.data = data
        self.level = level

    # method to generate child nodes from the current node
    def generate_child(self):
        x, y = self.find(self.data, 0)
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1)
                children.append(child_node)
        return children

    # method to shuffle the puzzle
    def shuffle(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = self.data[:]
            temp = temp_puz[x2*3 + y2]
            temp_puz[x2*3 + y2] = temp_puz[x1*3 + y1]
            temp_puz[x1*3 + y1] = temp
            return temp_puz
        else:
            return None

    # method to find the position of the empty spot in the puzzle
    def find(self, puz, x):
        return puz.index(x) // 3, puz.index(x) % 3


class Puzzle:
    # initialization method for Puzzle class
    def __init__(self, size):
        self.n = size

    # method to perform depth limited search
    def dls(self, start, goal, limit):
        stack = [(start, [])]

        while stack:
            state, path = stack.pop()

            if state.data == goal:
                return path

            if state.level < limit:
                for child in state.generate_child():
                    stack.append((child, path + [str(child.data)]))

        return "Goal not reachable within depth limit"


puz = Puzzle(3)
print("Enter the start state as a list of numbers from 0 to 8, where 0 represents the empty space:")
start_state = list(map(int, input().split()))
print("Enter the goal state as a list of numbers from 0 to 8, where 0 represents the empty space:")
goal_state = list(map(int, input().split()))
print("Enter the depth limit:")
depth_limit = int(input())

start = Node(start_state, 0)
print(puz.dls(start, goal_state, depth_limit))
