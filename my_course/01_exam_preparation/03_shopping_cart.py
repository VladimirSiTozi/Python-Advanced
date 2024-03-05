def shopping_cart(*args):
    all_meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    meal_limits = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    for current_meal in args:
        if current_meal == 'Stop':
            break

        meal, product = current_meal

        if len(all_meals[meal]) < meal_limits[meal]:
            if product not in all_meals[meal]:
                all_meals[meal].append(product)

    sorted_meals = sorted(all_meals.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ''

    if not all_meals['Soup'] and not all_meals['Pizza'] and not all_meals['Dessert']:
        return f'No products in the cart!'

    for meal, products in sorted_meals:
        result += f'{meal}:\n'
        for product in sorted(products, key=lambda x: x[0]):
            result += f' - {product}\n'

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
