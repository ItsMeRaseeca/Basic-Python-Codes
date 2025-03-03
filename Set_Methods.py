"""fruits = {"kiwi", "fig", "papaya"}
print(fruits)
fruits.add("orange")
print(fruits)

numbers = {12, 24, 33, 14}
print(numbers)
numbers.remove(33)
print(numbers)
"""
"""
animals = {"dog", "cat", "rabbit"}
animals.discard("cat")
print(animals)

colors = {"red", "blue", "green"}
print(colors)
removed_color = colors.pop()
print(removed_color)
print(colors)

mixed_set = {1, "apple", 3.14, True}
print(mixed_set)
mixed_set.clear()
print(mixed_set)

"""
"""
animals = {"dog", "cat", "rabbit"}
print(animals)
animals.discard("cat")
print(animals)


colors = {"red", "blue", "green"}
print(colors)
colors.update({"yellow", "purple", "blue"})
print(colors)



cities1 = {"New York", "London", "Paris"}
print(cities1)
cities2 = {"Tokyo", "Paris", "Berlin"}
print(cities2)
union_cities = cities1.union(cities2)
print(union_cities)

set1 = {1, 2, 3, 4}
print(set1)
set2 = {3, 4, 5, 6}
print(set2)
common_elements = set1.intersection(set2)
print(common_elements)


fruits1 = {"apple", "banana", "cherry"}
print(fruits1)
fruits2 = {"banana", "cherry", "orange"}
print(fruits2)
difference_fruits = fruits1.difference(fruits2)
print(difference_fruits)

letters1 = {"a", "b", "c"}
print(letters1)
letters2 = {"b", "c", "d"}
print(letters2)
sym_diff = letters1.symmetric_difference(letters2)
print(sym_diff)

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))


set1 = {1, 2, 3, 4}
print(set1)
set2 = {3, 4, 5, 6}
print(set2)
set1.intersection_update(set2)
print(set1) 
"""

fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "cherry", "orange"}
fruits1.difference_update(fruits2)
print(fruits1)  
