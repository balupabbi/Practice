#Stacks and Queue representation in python
#https://www.geeksforgeeks.org/using-list-stack-queues-python/


#Simple BFS python implementation: https://www.youtube.com/watch?v=QkEOGoUar3g
#Simple DFS python implementation: https://www.youtube.com/watch?v=0Zsabo7ires

from collections import deque

class Graph:
    def __init__(self, size):
        self.S = size
        self.adjacencylist = {}

    def add_edge(self, src, dst):

        if src in self.adjacencylist:
            neighbors = self.adjacencylist[src]
            neighbors.append(dst)
        else:
            self.adjacencylist[src] = [dst]

        if dst in self.adjacencylist:
            neighbors = self.adjacencylist[dst]
            neighbors.append(src)
        else:
            self.adjacencylist[dst] = [src]
        print("Done")

    def delete_edge(self):
        print("Deleted edge")

    def bfs(self, start):
        #Create a list with boolean values and index indicates node, Change the index to True if visited
        #Keep adding all the adjacent nodes in the queue as you are looping through the queue until it is empty

        if start not in self.adjacencylist.keys():
            print("Starting node not found in existing graph")
            return

        visited = [False]*len(self.adjacencylist.keys())
        queue = deque()
        current_node = start
        visited[current_node] = True
        queue.append(start)

        while queue:
            current_node = queue.popleft()
            print("Current Node Investigation: {}".format(current_node))

            neighbors_start = self.adjacencylist[current_node]

            for node in neighbors_start:
                if visited[node] == True:
                    continue
                else:
                    visited[node] = True
                    if node not in queue:
                        queue.append(node)

        if all( i == True for i in visited):
            print("bfs is DONE and visited all nodes")
            return
        else:
            print("Something is fishy")

    def dfs(self, start):
        #Very similar to BFS but you use stack and this way you are traversing through graph by going in depth
        visited = [False]*len(self.adjacencylist.keys())
        stack = []
        stack.append(start)

        while stack:
            current_node = stack.pop()
            print("Current node: {}".format(current_node))
            for neighbor in self.adjacencylist[current_node]:
                if visited[neighbor]:
                    continue
                else:
                    if neighbor not in stack:
                        stack.append(neighbor)
            visited[current_node] = True


        if all(True for i in visited):
            print("Done with dfs")

    def recursive_dfs(self, start, visited=[]):

        if visited:
            if all(i==True for i in visited):
                print("all done")
                return
            # mark it as visited if we haven't seen it before
            if visited[start]:
                return
            else:
                visited[start] = True
                print("Node visited: {}".format(start))
                # make a recursive call for all its neighbors
                for neighbor in self.adjacencylist[start]:
                    self.recursive_dfs(neighbor, visited)

        else:
            visited = [False] * len(self.adjacencylist)
            self.recursive_dfs(start,visited)





    def find_shortest_path(self, start, end):

        print("Finding shortest path")









if __name__ == "__main__":
    # vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # edgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6)]
    # graphs = (vertexList, edgeList)
    #
    # print(bfs(graphs, 0))
    size = 5
    graph = Graph(5)
    graph.add_edge(0,4)
    graph.add_edge(0,1)
    graph.add_edge(1,4)
    graph.add_edge(1,3)
    graph.add_edge(3,4)
    graph.add_edge(2,3)
    graph.add_edge(1,2)
    print (graph.adjacencylist)

    graph.recursive_dfs(0)
