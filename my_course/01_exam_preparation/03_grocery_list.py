def shop_from_grocery_list(budget, *args):
    grocery_list = args[0]
    bought_products = []
    for products in args[1::]:
        product_name = products[0]
        price = products[1]
        if product_name in grocery_list:
            if product_name not in bought_products:
                if price <= budget:
                    budget -= price
                    bought_products.append(product_name)
                else:
                    break

    if len(grocery_list) == len(bought_products):
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        missing_products = set(grocery_list).symmetric_difference(set(bought_products))
        result = ''
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
