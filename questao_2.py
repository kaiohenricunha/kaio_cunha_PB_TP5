import heapq

def prim(graph, start):
    mst = []                    # Lista para armazenar as arestas da MST
    visited = set([start])      # Conjunto de vértices já incluídos na MST
    # Fila de prioridade para as arestas (peso, vértice de origem, vértice destino)
    edges = []
    
    # Inicialmente, adiciona todas as arestas a partir do vértice inicial
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))
    
    # Enquanto houver arestas e nem todos os vértices estiverem visitados
    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            # Adiciona todas as arestas que partem do vértice recém-adicionado
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    return mst

# Exemplo de uso:
if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 4)],
        'C': [('A', 3), ('B', 1), ('D', 5)],
        'D': [('B', 4), ('C', 5)]
    }
    start = 'A'
    mst = prim(graph, start)
    
    print("Árvore Geradora Mínima (MST):")
    for u, v, weight in mst:
        print(f"{u} - {v} com peso {weight}")
