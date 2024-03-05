def forecast(*args):
    cities = {}
    weather_sort_order = {"Sunny": 0, "Cloudy": 1, "Rainy": 2}
    for data in args:
        city, weather = data[0], data[1]
        cities[city] = weather

    sorted_cities = dict(sorted(cities.items(), key=lambda kvp: (weather_sort_order[kvp[1]], kvp[0])))

    result = ''
    for city, weather in sorted_cities.items():
        result += f'{city} - {weather}\n'

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


