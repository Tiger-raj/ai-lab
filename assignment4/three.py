from queue import PriorityQueue

# number of vertices in the graph
v = 14

# initialize the graph
graph = [[] for i in range(v)]

# heuristic values for each node
heuristic = [16,37,20,10,25,26,7,0,2,4,5,6]

def Astar_search(actual_Src, target, n):
    # initialize visited nodes
    visited = [False] * n

    # initialize priority queue
    pq = PriorityQueue()

    # add source to priority queue
    pq.put((heuristic[0], actual_Src))

    # mark source as visited
    visited[actual_Src] = True
     
    # while priority queue is not empty
    while pq.empty() == False:
        # get the node with the lowest heuristic value
        u = pq.get()[1]

        # print the current node
        print(u, end=" ")

        # if the current node is the target, break the loop
        if u == target:
            break
        
        # clear the priority queue
        while (pq.empty() == False):
            pq.get()
 
        # for each neighbor of the current node
        for i in range(len(graph[u])):
            v,cost=graph[u][i]
            # if the neighbor has not been visited
            if visited[v] == False:
                # mark the neighbor as visited
                visited[v] = True

                # add the neighbor to the priority queue
                pq.put((heuristic[v]+cost, v))

    # print a newline
    print()


def addedge(x, y, cost):
    # add an edge to the graph
	graph[x].append((y, cost))
	graph[y].append((x, cost))

# add edges to the graph
addedge(0, 1, 2)
addedge(0, 2, 3)
addedge(0, 3, 6)
addedge(1, 4, 7)
addedge(1, 5, 8)
addedge(2, 6, 5)
addedge(2, 7, 8)
addedge(3, 8, 9)
addedge(8, 9, 4)
addedge(8, 10, 2)
addedge(9, 11, 1)
addedge(9, 12, 6)
addedge(9, 13, 1)

# set the source and target nodes
source = 0
target = 9

# print the path to the goal
print("Path to goal is (using A* search) : ")

# call the A* search function
Astar_search(source, target, v)
