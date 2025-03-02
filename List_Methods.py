countries = ["India", "USA", "Canada", "Australia", "Germany"]
print(countries)
countries.append("Japan")
print(countries) 


mixed_list = [1, "apple", True, 3.14]
print(mixed_list)
mixed_list.clear()
print(mixed_list)


animals = ["cat", "tiger", "lion"]
print(animals)
animals_copy = animals.copy()
print(animals_copy)


bool_list = [True, False, True, True, False]
print(bool_list.count(True))

numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)


colors = ["red", "blue", "green", "yellow"]
print(colors.index("green"))



bool_list = [True, False, True]
print(bool_list)
bool_list.insert(1, False)
print(bool_list)

countries = ["India", "USA", "Canada", "Germany"]
removed_country = countries.pop(2)
print(removed_country)
print(countries)



numbers = [10, 22, 30, 22, 43]
print(numbers)
numbers.remove(22)
print(numbers)

mixed_list = [1, "hello", 3.5, False]
mixed_list.reverse()
print(mixed_list)


animals = ["dog", "cat", "elephant", "bear"]
print(animals)
animals.sort()
print(animals)
