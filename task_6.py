# Define items with their respective costs and calories
menu_items = {
    "pizza": {"price": 50, "calories": 300},
    "hamburger": {"price": 40, "calories": 250},
    "hot-dog": {"price": 20, "calories": 200},
    "pepsi": {"price": 10, "calories": 100},
    "cola": {"price": 15, "calories": 220},
    "potato": {"price": 25, "calories": 350}
}

def greedy_selection(menu_items, budget_limit):
    sorted_menu = sorted(menu_items.items(), key=lambda x: x[1]['calories'] / x[1]['price'], reverse=True)
    chosen_items = []
    total_calories = 0
    total_spent = 0

    for item, details in sorted_menu:
        if total_spent + details['price'] <= budget_limit:
            chosen_items.append(item)
            total_spent += details['price']
            total_calories += details['calories']

    return chosen_items, total_calories, total_spent

def dp_selection(menu_items, budget_limit):
    num_items = len(menu_items)
    dp_table = [[0 for _ in range(budget_limit + 1)] for _ in range(num_items + 1)]
    item_list = list(menu_items.items())

    for i in range(1, num_items + 1):
        for cost in range(budget_limit + 1):
            if item_list[i-1][1]['price'] <= cost:
                dp_table[i][cost] = max(item_list[i-1][1]['calories'] + dp_table[i-1][cost-item_list[i-1][1]['price']], dp_table[i-1][cost])
            else:
                dp_table[i][cost] = dp_table[i-1][cost]

    total_calories = dp_table[num_items][budget_limit]
    cost = budget_limit
    chosen_items = []

    for i in range(num_items, 0, -1):
        if total_calories <= 0:
            break
        if total_calories == dp_table[i-1][cost]:
            continue
        else:
            chosen_items.append(item_list[i-1][0])
            total_calories -= item_list[i-1][1]['calories']
            cost -= item_list[i-1][1]['price']

    total_spent = budget_limit - cost
    return chosen_items, dp_table[num_items][budget_limit], total_spent

# Example usage
budget_limit = 100

# Greedy algorithm results
items_greedy, calories_greedy, cost_greedy = greedy_selection(menu_items, budget_limit)
print(f"Greedy Selection: {items_greedy}, Total Calories: {calories_greedy}, Total Cost: {cost_greedy}")

# Dynamic programming results
items_dp, calories_dp, cost_dp = dp_selection(menu_items, budget_limit)
print(f"Dynamic Programming Selection: {items_dp}, Total Calories: {calories_dp}, Total Cost: {cost_dp}")