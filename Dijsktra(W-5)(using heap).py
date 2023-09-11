import heapq
import sys
def dijsktra (graph,start):
    distances = {node: sys.maxsize for node in graph}
    heap = [(0,start)]
    distances[start] = 0
    while heap:
        (distance ,current) = heapq.heappop(heap)
        if distance > distances[current]:
            continue
        for neighbour,weight in graph[current].items():
            dist = distance + weight
            if dist< distances[neighbour]:
                distances[neighbour] = dist
                heapq.heappush(heap,(dist,neighbour))
    print("Vertex \t Distance")
    for i in distances:
        print(i, ' \t ',distances[i])
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8, 3: 7, 5: 4, 8: 2},
    3: {2: 7, 5: 14, 4: 9},
    4: {5: 10, 3: 9},
    5: {2: 4, 3: 14, 4: 10, 6: 2},
    6: {5: 2, 8: 6, 7: 1},
    7: {6: 1, 8: 7, 0: 8, 1: 11},
    8: {2: 2, 6: 6, 7: 7}
}

dijsktra(graph,0)
