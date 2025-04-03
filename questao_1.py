import heapq

def dijkstra(graph, source):
    # Inicializa todas as distâncias como infinito, exceto o vértice de origem
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0

    # Fila de prioridade com tuplas (distância, vértice)
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Se a distância atual for maior que a registrada, pula para a próxima iteração
        if current_distance > distances[current_vertex]:
            continue
        
        # Relaxa as arestas a partir do vértice atual
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Exemplo de uso:
if __name__ == '__main__':
    # Definição do grafo
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    source = 'A'
    distances = dijkstra(graph, source)
    
    # Exibe os resultados
    for vertex, distance in distances.items():
        print(f"Distância até {vertex}: {distance}")
