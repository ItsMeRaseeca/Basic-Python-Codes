# Example 1: get()
employee = {"id": 101, "name": "Alice", "department": "HR"}
print(employee.get("name"))  # Output: Alice

# Example 2: keys()
person = {"first_name": "Raseeca", "last_name": "Kashelkar", "age": 19}
print(person.keys())  # Output: dict_keys(['first_name', 'last_name', 'age'])

# Example 3: values()
student = {"name": "Raseeca", "last_name": "Kashelkar", "age": 19}
print(student.values())  # Output: dict_values(['Bob', 'A', 20])

# Example 4: items()
book = {"title": "Operating System", "author": "Galvin, Silberchatz", "year": 2003}
print(book.items())  # Output: dict_items([('title', '1984'), ('author', 'George Orwell'), ('year', 1949)])

# Example 5: update()
fruits = {"apple": 50, "banana": 30}
print(fruits)
fruits.update({"orange": 40, "banana": 35})
print(fruits)


# Example 6: pop()
person = {"name": "Raseeca", "age": 19, "city": "Mumbai"}
print(person)
removed_value = person.pop("age")
print(removed_value)  
print(person)  # Output: {'name': 'Charlie', 'city': 'New York'}


# Example 7: popitem()
config = {"host": "localhost", "port": 8080, "debug": True}
last_item = config.popitem()
print(last_item)  # Output: ('debug', True)
print(config)  # Output: {'host': 'localhost', 'port': 8080}



# Example 8: setdefault()
settings = {"theme": "dark", "language": "English"}
print(settings.setdefault("font_size", 14))  # Output: 14 (new key added)
print(settings)  # Output: {'theme': 'dark', 'language': 'English', 'font_size': 14}


# Example 9: clear()
data = {"letters": "ABC", "numbers": "123"}
print(data)
data.clear()
print(data)  # Output: {}

# Example 10: copy()
profile = {"username": "raseeca", "roll_number": "143"}
print(profile)
profile_copy = profile.copy()
print(profile_copy)  # Output: {'username': 'admin', 'access': 'full'}

# Example 11: fromkeys()
keys = ["id", "name", "status"]
new_dict = dict.fromkeys(keys, "unknown")
print(new_dict)  # Output: {'id': 'unknown', 'name': 'unknown', 'status': 'unknown'}

# Example 12: del
user = {"username": "raseeca123", "email": "raseecakashelkar163@gmail.com", "age": 19}
print(user)
del user["age"]
print(user)  # Output: {'username': 'jane_doe', 'age': 28}"""

person = dict(name="Raseeca", age=19, city="Mumbai")
print(person)
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car)

print(car["model"])


car["color"] = "blue"
print(car)
