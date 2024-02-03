def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    selected_items = []
    remaining_budget = budget

    for item_name, properties in sorted_items:
        if properties["cost"] <= remaining_budget:
            selected_items.append(item_name)
            remaining_budget -= properties["cost"]

    return selected_items

def dynamic_programming(items, budget):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            item_cost = items[list(items.keys())[i - 1]]["cost"]
            item_calories = items[list(items.keys())[i - 1]]["calories"]

            if item_cost <= j:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - item_cost] + item_calories)
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    selected_items = []
    i, j = num_items, budget

    while i > 0 and j > 0:
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return selected_items[::-1]

if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    #  бюджет
    budget = 70

    # Виклик жадібного алгоритму та виведення результату
    greedy_result = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:", greedy_result)

    # Виклик алгоритму динамічного програмування та виведення результату
    dp_result = dynamic_programming(items, budget)
    print("Dynamic Programming Result:", dp_result)
