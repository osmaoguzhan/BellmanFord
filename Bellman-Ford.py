import time
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # adding an edge
    def addEdge(self, u, v, weight):
        self.graph.append([u, v, weight])

    #print the solution
    def Solution(self, dist):
        print("\nResult for the Shortest Path")
        print("--------------------")
        print(" Vertex   Distance  ")
        print("--------------------")
        for i in range(self.V):
            print("% d \t\t % .0f" % (i, dist[i]))

    #printing step by step
    def Memory(self, dist):
        print("\r"+ str(dist),end=" ")
        time.sleep(1)

    def BellmanFord(self, source):
        #initialization:
        # sets the distances to each vertex in the graph to infinity.
        # sets the source to 0
        distance = [float("Inf")] * self.V
        distance[source] = 0
        #simply goes through each edge (u, v) in E and relaxes it.
        # This process is done |V| - 1
        for i in range(self.V - 1):
            for u, v, weight in self.graph:
                if distance[u] != float("Inf") and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    self.Memory(distance)
        #detection of the negative weight cycle.
        for u, v, weight in self.graph:
            if distance[u] != float("Inf") and distance[u] + weight < distance[v]:
                print ("\nnegative weight cycle!!")
                return

        #printing all results
        self.Solution(distance)

print("non negative cycle example")
g = Graph(6)

g.addEdge(0, 1, 8)
g.addEdge(0, 2, 10)
g.addEdge(1, 3, 1)
g.addEdge(2, 4, 2)
g.addEdge(3, 2, -4)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
g.addEdge(5, 2, 1)

g.BellmanFord(0)

print("negative cycle example")
g = Graph(3)

g.addEdge(0, 2, 3)
g.addEdge(2, 1, 2)
g.addEdge(1, 0, -6)

g.BellmanFord(0)