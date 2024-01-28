procedure BFS(start_vertex):
    initialize an empty queue
    enqueue start_vertex into the queue
    mark start_vertex as visited
    while the queue is not empty:
        current_vertex = dequeue from the queue
        process current_vertex (optional)
        for each neighbor in adjacency_list[current_vertex]:
            if neighbor is unvisited:
                mark neighbor as visited
                enqueue neighbor into the queue