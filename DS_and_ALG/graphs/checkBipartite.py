"""
leetcode: https://leetcode.com/problems/is-graph-bipartite/

0---1
|   |
3-- 2

A B
0 1
2 3
"""




def checkBipartite_bfs(nodes):

    """
    Checks if graph is bipartite
    :return:
    """
    colors = {}

    for node in range(len(nodes)):
        if node not in colors:
            colors[node] = 0
            queue = [node]

            while queue:
                #need to get all the neighbors
                node = queue.pop(0)
                for nei in nodes[node]:
                    #need to check colors
                    if nei in colors:
                        if colors[nei] == colors[node]:
                            return False
                    else:
                        #add neighbor to color
                        colors[nei]=1-colors[node]
                        queue.append(nei)

    return True




def checkBipartite_dfs(graph):

    color = {}
    for node in range(len(graph)):

        if node not in color:
            #iterative dfs
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if nei not in color:
                        color[nei] = 1-color[node]
                        stack.append(nei)
                    elif color[nei] == color[node]:
                        return False

    return True

"""
1---2--4
|
3
"""



def checkBipartite_dfs_recursive(graph):

    color = {}

    def dfs(node):
        #traverse through neighbors recursively
        # this function checks if it is bipartite or not

        for nei in graph[node]:
            if nei in color:
                if color[nei] == color[node]:
                    return False
            else:
                color[nei] = 1-color[node]
                if not dfs(nei):
                    return False
                #return dfs(nei)

        return True




    for node in range(len(graph)):

        # we will color it if node not in colors
        # we will traverse dfs recursive and check if it is bipartite, return False if it isn't bipartite
        #
        if node not in color:
            color[node] = 0

            if not dfs(node):
                return False

    return True








if __name__ == "__main__":
    nodes = [[1, 3], [0, 2], [1, 3], [0, 2]]
    nodes = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    nodes = [[3,4,6],[3,6],[3,6],[0,1,2,5],[0,7,8],[3],[0,1,2,7],[4,6],[4],[]]
    if(checkBipartite_dfs_recursive(nodes)):
        print("Yes it is Bipartite")
    else:
        print("Not Bipartite")