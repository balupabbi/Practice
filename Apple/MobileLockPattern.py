


def dfs(start):

    adj={0:[2,4], 2:[1,3], 4:[1,3], 3:[2,4], 1:[2,4]}

    visited = [False]*len(adj.keys())
    stack = []
    stack.append(start)

    while stack:
        current = stack.pop()

        n = adj[current]

        if not visited[current]:
            print(current)
            for node in n:
                stack.append(node)
        else:
            continue

        #update visited
        visited[current] = True

    if all(visited):
        print('Done')




def mobileLockPattern():
    """0

    :return:
    """

    return




if __name__ == "__main__":
    dfs(0)