#solve using Bidirectional search
from queue import Queue

# checks if the current state is the goal state
def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# generates all possible moves from the current state
def get_possible_moves(state):
    possible_moves = []
    # find the index of the zero tile
    zero_index = [(index, row.index(0)) for index, row in enumerate(state) if 0 in row][0]

    # check if moving the zero tile up is a valid move
    if zero_index[0] > 0:  
        # create a copy of the current state
        new_state = [row[:] for row in state]
        # swap the zero tile with the tile above it
        new_state[zero_index[0]][zero_index[1]], new_state[zero_index[0] - 1][zero_index[1]] = new_state[zero_index[0] - 1][zero_index[1]], new_state[zero_index[0]][zero_index[1]]
        # add the new state to the list of possible moves
        possible_moves.append(new_state)
    # check if moving the zero tile left is a valid move
    if zero_index[1] > 0:  
        new_state = [row[:] for row in state]
        new_state[zero_index[0]][zero_index[1]], new_state[zero_index[0]][zero_index[1] - 1] = new_state[zero_index[0]][zero_index[1] - 1], new_state[zero_index[0]][zero_index[1]]
        possible_moves.append(new_state)
    # check if moving the zero tile down is a valid move
    if zero_index[0] < 2:  
        new_state = [row[:] for row in state]
        new_state[zero_index[0]][zero_index[1]], new_state[zero_index[0] + 1][zero_index[1]] = new_state[zero_index[0] + 1][zero_index[1]], new_state[zero_index[0]][zero_index[1]]
        possible_moves.append(new_state)
    # check if moving the zero tile right is a valid move
    if zero_index[1] < 2:  
        new_state = [row[:] for row in state]
        new_state[zero_index[0]][zero_index[1]], new_state[zero_index[0]][zero_index[1] + 1] = new_state[zero_index[0]][zero_index[1] + 1], new_state[zero_index[0]][zero_index[1]]
        possible_moves.append(new_state)

    return possible_moves

# prints the current state
def print_state(state):
    for row in state:
        print(' '.join(str(cell) for cell in row))
    print()

# performs a bidirectional search from the initial state to the goal state
def bidirectional_search(initial_state, goal_state):
    # if the initial state is the goal state, return an empty path
    if initial_state == goal_state:
        return []

    # initialize the forward search
    forward_queue = Queue()
    forward_queue.put((initial_state, []))
    forward_visited = set()
    forward_visited.add(str(initial_state))

    # initialize the backward search
    backward_queue = Queue()
    backward_queue.put((goal_state, []))
    backward_visited = set()
    backward_visited.add(str(goal_state))

    # continue searching as long as there are states to explore in both directions
    while not forward_queue.empty() and not backward_queue.empty():
        # explore the next state in the forward direction
        forward_state, forward_path = forward_queue.get()
        for move in get_possible_moves(forward_state):
            # skip this state if it has already been visited in the forward direction
            if str(move) in forward_visited:
                continue
            # if this state has been visited in the backward direction, a solution has been found
            if str(move) in backward_visited:
                print("Meeting point:")
                print_state(move)
                # return the path from the initial state to the goal state
                backward_state, backward_path = backward_queue.queue[list(backward_visited).index(str(move))]
                return forward_path + [move] + backward_path[::-1]
            # add this state to the forward queue and mark it as visited in the forward direction
            forward_queue.put((move, forward_path + [move]))
            forward_visited.add(str(move))

        # explore the next state in the backward direction
        backward_state, backward_path = backward_queue.get()
        for move in get_possible_moves(backward_state):
            # skip this state if it has already been visited in the backward direction
            if str(move) in backward_visited:
                continue
            # if this state has been visited in the forward direction, a solution has been found
            if str(move) in forward_visited:
                print("Meeting point:")
                print_state(move)
                # return the path from the initial state to the goal state
                forward_state, forward_path = forward_queue.queue[list(forward_visited).index(str(move))]
                return forward_path + [move] + backward_path[::-1]
            # add this state to the backward queue and mark it as visited in the backward direction
            backward_queue.put((move, backward_path + [move]))
            backward_visited.add(str(move))

    # if no solution was found, return None
    return None

# input the initial state from the terminal
print("Enter the initial state matrix:")
initial_state = [list(map(int, input().split())) for _ in range(3)]

# input the goal state from the terminal
print("Enter the goal state matrix:")
goal_state = [list(map(int, input().split())) for _ in range(3)]

# find a solution from the initial state to the goal state
solution = bidirectional_search(initial_state, goal_state)
# if a solution was found, print the path from the initial state to the goal state
if solution is not None:
    print("Initial state:")
    print_state(initial_state)
    for state in solution:
        print("Next move:")
        print_state(state)
# if no solution was found, print a message
else:
    print("No solution found.")
