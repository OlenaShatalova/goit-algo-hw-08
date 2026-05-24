import heapq

def min_cost_connect_cables(cables):
    """Повертає мінімальні загальні витрати на з'єднання всіх кабелів.

    Алгоритм: завжди з'єднуємо два найкоротші кабелі.
    Складність: O(n log n)
    """
    if len(cables) == 0:
        return 0
    if len(cables) == 1:
        return cables[0]

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        cost = first + second
        total_cost += cost

        print(f"З'єднуємо {first} + {second} = {cost} (Витрати загалом: {total_cost})")

        heapq.heappush(heap, cost)

    return total_cost


# Тест
if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    result = min_cost_connect_cables(cables)

    print(f"Мінімальні загальні витрати: {result}") # Очікується: 29