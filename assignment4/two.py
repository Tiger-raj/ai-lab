from queue import PriorityQueue

# function to calculate heuristic based on misplaced tiles
def heuristic(state, target):
    return sum(s != t for s, t in zip(state, target) if s != 0)

# function to print the current state of the puzzle
def print_state(state):
    print("\n".join(str(state[n:n+3]) for n in range(0, len(state), 3)))

# A* search algorithm
def astar(src, target):
    # initialize the priority queue with the source state
    states_queue = PriorityQueue()
    states_queue.put((heuristic(src, target), 0, "", src))

    # set to keep track of visited states
    visited_states = set()

    # while there are states to explore
    while not states_queue.empty():
        # get the state with the lowest cost so far
        _, moves_so_far, path_so_far, current_state = states_queue.get()

        # print the current state
        print_state(current_state)
        print("\n")

        # if the current state is the target state, return the path so far
        if current_state == target:
            return path_so_far

        # generate all possible next states
        for (dx, dy, move) in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            # find the position of the empty tile
            x, y = current_state.index(0) // 3, current_state.index(0) % 3

            # calculate the new position of the empty tile
            newx, newy = x + dx, y + dy

            # if the new position is valid
            if 0 <= newx < 3 and 0 <= newy < 3:
                # create a copy of the current state
                new_state = current_state[:]

                # move the tile
                new_state[x*3+y], new_state[newx*3+newy] = new_state[newx*3+newy], new_state[x*3+y]

                # if the new state has not been visited yet
                if tuple(new_state) not in visited_states:
                    # add the new state to the queue
                    states_queue.put((moves_so_far + 1 + heuristic(new_state, target), moves_so_far + 1, path_so_far + move, new_state))

                    # mark the new state as visited
                    visited_states.add(tuple(new_state))

    # if no solution was found
    return "No solution found"

# initial state of the puzzle
src = [1, 2, 3, 5, 6, 0, 7, 8, 4]

# target state of the puzzle
target = [1, 2, 3, 5, 8, 6, 0, 7, 4]

# find the path from the initial state to the target state
path=astar(src, target)

# print the path
print("Path so far :",path)
