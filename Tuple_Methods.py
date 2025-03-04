numbers = (1, 2, 2, 3, 4, 2)
print(numbers.count(2))

cities = ("New York", "London", "Tokyo", "London")
print(cities.index("London"))


colors1 = ("red", "blue", "yellow")
print(colors1)
colors2 = ("green", "purple", "orange")
print(colors2)
colors = colors1 + colors2
print(colors)

languages = ("Python", "Java", "C++", "JavaScript", "Ruby")
print(languages)
print(languages[1:4])

mixed_list = (True, 42, "Hello", 3.14)
print(mixed_list)
print(len(mixed_list))

coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)

fruits = ("Pineapple", "Strawberry", "Kiwi")
(yellow, red, green) = fruits
print(red)

car = ("Tesla", ("Model 3", 2023), "Electric")
print(car[1])
print(car[1][1])

animals = ("cat", "dog", "rabbit")
animals_list = list(animals)
animals_list.append("parrot")
animals = tuple(animals_list)
print(animals)

numbers = (7, 2, 5, 1, 9)
print(numbers)
sorted_numbers = tuple(sorted(numbers))
print(sorted_numbers)
