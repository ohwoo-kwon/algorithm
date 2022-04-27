import queue

INF = 1000000000


def dijkstra(n, graph, src, dst, traps):
    pq = queue.PriorityQueue()
    visited = [[False for _ in range((1 << len(traps) - 1) + 1)] for _ in range(n + 1)]
    pq.put((0, src, 0))

    while not pq.empty():
        curr = pq.get()
        w = curr[0]  # 비용
        u = curr[1]  # 노드 번호
        state = curr[2]  # 그래프 상태

        if u == dst:
            return w
        if visited[u][state]:
            continue
        visited[u][state] = True

        currTrapped = False
        trapped = {}
        for i in range(len(traps)):
            bit = 1 << i;
            if state & bit:
                if u == traps[i]:
                    state &= ~bit
                else:
                    trapped[traps[i]] = True
            else:
                if u == traps[i]:
                    state |= bit
                    trapped[traps[i]] = True
                    currTrapped = True

        for v in range(1, n + 1):
            if v == u:
                continue
            nextTrapped = True if v in trapped else False
            if currTrapped == nextTrapped:
                if graph[u][v] != INF:
                    pq.put((w + graph[u][v], v, state))
            else:
                if graph[v][u] != INF:
                    pq.put((w + graph[v][u], v, state))


def solution(n, start, end, roads, traps):
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for road in roads:
        u = road[0]
        v = road[1]
        w = road[2]
        if w < graph[u][v]:
            graph[u][v] = w

    return dijkstra(n, graph, start, end, traps)