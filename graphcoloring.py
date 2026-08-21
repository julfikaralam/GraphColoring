def is_safe(graph, node, color, c):
    # Check adjacent vertices
    for i in range(len(graph)):
        if graph[node][i] == 1 and color[i] == c:
            return False

    return True


def graph_coloring(graph, k, color, node=0):

    if node == len(graph):
        return True


    for c in range(1, k + 1):

        if is_safe(graph, node, color, c):

            color[node] = c


            if graph_coloring(graph, k, color, node + 1):
                return True

            color[node] = 0


    return False



with open("input.txt", "r") as file:

    T = int(file.readline())


    for case in range(1, T + 1):

        N, M, K = map(int, file.readline().split())

        graph = [[0 for _ in range(N)] for _ in range(N)]

        for _ in range(M):

            u, v = map(int, file.readline().split())

            graph[u][v] = 1
            graph[v][u] = 1


        color = [0] * N

        print(f"Case #{case}:")


        if graph_coloring(graph, K, color):

            print(f"Coloring Possible with {K} Colors")
            print("Color Assignment:", color)

        else:

            print(f"Coloring Not Possible with {K} Colors")

    print()