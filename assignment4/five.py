# function to calculate heuristic based on the number of blocks in correct position
def heuristic(state, goal):
    score = 0
    for i in range(len(state)):
        if state[i] == goal[i]:
            score += 1
        else:
            score -= 1
    return score

# hill climbing algorithm
def hill_climbing(initial_state, goal_state):
    # start from the initial state
    current_state = initial_state

    # while the current state is not the goal state
    while current_state != goal_state:
        # print the current state
        print(current_state)

        # get all neighbors of the current state
        neighbors = get_neighbors(current_state)

        # choose the neighbor with the highest heuristic value as the next state
        next_state = max(neighbors, key=lambda state: heuristic(state, goal_state))

        # if the heuristic value of the next state is not greater than the current state, return the current state
        if heuristic(next_state, goal_state) <= heuristic(current_state, goal_state):
            return current_state

        # move to the next state
        current_state = next_state

    # return the current state
    return current_state

# function to generate all neighbors of a state
def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and state[i]:
                # copy the current state to generate a new neighbor
                new_state = [stack[:] for stack in state]

                # move the top block from stack i to stack j
                new_state[j].append(new_state[i].pop())

                # add the new state to the list of neighbors
                neighbors.append(new_state)
    return neighbors

# initial state of the blocks
initial_state = [[1, 2,4], [3], []]

# goal state of the blocks
goal_state = [[], [], [1, 2, 4,3]]

# run the hill climbing algorithm and print the result
print(hill_climbing(initial_state, goal_state))
