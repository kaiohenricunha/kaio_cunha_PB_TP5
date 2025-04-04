import math

def euclidean_distance(coord1, coord2):
    """
    Calcula a distância Euclidiana entre duas coordenadas (x, y).
    """
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def tsp_nearest_neighbor(cities, start_city):
    """
    Resolve o Problema do Caixeiro Viajante usando a heurística do vizinho mais próximo.

    Parâmetros:
    - cities: dicionário onde cada chave é o nome da cidade e o valor é uma tupla (x, y).
    - start_city: cidade inicial para começar a rota.

    Retorna:
    - route: lista com a ordem das cidades visitadas.
    """
    unvisited = set(cities.keys())
    route = [start_city]
    current_city = start_city
    unvisited.remove(start_city)

    while unvisited:
        # Seleciona a cidade não visitada mais próxima da cidade atual
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        route.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    return route

# Exemplo de uso:
if __name__ == "__main__":
    cities = {
        "A": (0, 0),
        "B": (1, 5),
        "C": (5, 2),
        "D": (6, 6),
        "E": (8, 3)
    }
    start_city = "A"
    route = tsp_nearest_neighbor(cities, start_city)
    print("Rota obtida pelo algoritmo:", "->".join(route))
