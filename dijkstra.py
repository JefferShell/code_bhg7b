
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# 测试
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"从节点 {start_node} 到各节点的最短距离:")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")
