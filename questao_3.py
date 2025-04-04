def knapsack_greedy(items, capacity):
    # Ordena os itens pela razão valor/peso em ordem decrescente
    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    
    chosen = []
    total_weight = 0
    total_value = 0
    
    # Itera pelos itens ordenados e adiciona-os à mochila se couberem
    for name, weight, value in sorted_items:
        if total_weight + weight <= capacity:
            chosen.append((name, weight, value))
            total_weight += weight
            total_value += value
    
    return chosen, total_weight, total_value

# Exemplo de uso:
if __name__ == "__main__":
    # Itens disponíveis: (nome, peso, valor)
    items = [
        ("item1", 2, 40),
        ("item2", 3, 50),
        ("item3", 5, 100),
        ("item4", 4, 90)
    ]
    capacity = 8
    
    chosen, total_weight, total_value = knapsack_greedy(items, capacity)
    
    print("Itens escolhidos:")
    for item in chosen:
        print(f"{item[0]}: peso {item[1]}, valor {item[2]}")
    
    print(f"\nPeso total: {total_weight}")
    print(f"Valor total: {total_value}")
