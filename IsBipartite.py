def isBipartite(graph):
    color = {}

    for node in range(len(graph)):
        if node not in color:
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
    return True


# isBipartite([[1,3],[0,2],[1,3],[0,2]])



