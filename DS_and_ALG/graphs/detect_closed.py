


class Graph():
    def __init__(self,size):
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

    def dfs(self, start):
        """
        traversing graph using dfs
        :param start:
        :return:
        """

        visited = [False]*self.S
        stack = []
        stack.append(start)

        while stack:
            cn = stack.pop()

            print("Current node: {}".format(cn))

            for node in self.adjacencylist[cn]:
                if visited[node]:
                    continue
                else:
                    if node not in stack:
                        stack.append(node)

            #mark cn as visited
            visited[cn] = True


    def checkClosedLoop(self, start):

        """

        Use dfs
        1) keep track of parent node while iterating throught the graph
        2) if u land on the node where parent node is neighbor and other neighbors are also visited then it is a loop
        :param start:
        :return:
        """

        visited = [False]*self.S
        stack = []
        stack.append(start)
        pn = -1

        while stack:
            cn = stack.pop()

            neighbors = self.adjacencylist[cn]

            check = True
            if pn in neighbors:
                #if this is the case, you know pn is already visited
                #check if all neighbors are also visited
                for node in neighbors:
                    if not visited[node]:
                        check = False

            if check:
                print("There is a closed loop")
                break

            for node in neighbors:
                if visited[node]:
                    continue
                else:
                    stack.append(node)

            visited[cn] = True
            pn = cn


        pass









if __name__ == "__main__":
    # vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # edgeList = [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (1, 6)]
    # graphs = (vertexList, edgeList)
    #
    # print(bfs(graphs, 0))
    graph = Graph(4)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(0,2)

    graph.checkClosedLoop(0)
