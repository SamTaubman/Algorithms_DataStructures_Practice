procedure DFS(vertex):
    if vertex is unvisited:
        mark vertex as visited
        process vertex (optional)
        for each neighbor in adjacency_list[vertex]:
            if neighbor is unvisited:
                DFS(neighbor)