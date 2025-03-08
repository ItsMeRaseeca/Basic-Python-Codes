
import csv
"""
file1 = open("phrases.txt")

file_content = file1.read()
print(file_content)

file1.close()

"""
"""
file2 = open("phrases.txt", 'w')
file2.write("You reap what you sow.")
file2.write("\nIt is what it is.")

file2 = open("phrases.txt", 'r')
file2_content = file2.read()
print(file2_content)

file2.close()

"""
"""
with open("StudentData.csv", mode = 'r') as file:
    file_content = csv.reader(file)

    header = next(file_content)
    print(f"Header Names: {header}", header)

    for row in file_content:
        print(row)

with open("Employee.csv", mode = 'w', newline = '') as file:
    writefile = csv.writer(file)

    header = ['Emp ID', 'Name', 'Department', 'Salary']
    writefile.writerow(header)

    data = [
        [1001, 'Raseeca', 'IT', 75000],
        [1002, 'Sasha Braus', 'HR', 67000],
        [1003, 'Levi Ackerman', 'Finance', 85000],
        [1004, 'Eren Yaeger', 'Customer Support', 54000],
        [1005, 'Mikasa Ackerman', 'Operations', 62000],
        [1006, 'Armin Arlert', 'Sales', 90000]]

    writefile.writerows(data)

"""
"""
with open("cities.txt", "w") as file:
    file.write("London\nParis\nNew York\nTokyo\nBerlin\nSydney")

def sort_cities(input_file, output_file):
    with open(input_file, "r") as file:
        cities = file.readlines()

    cities = [city.strip() for city in cities] 

    with open(output_file + "_asc.txt", "w") as file:
        file.write("\n".join(sorted(cities)))

    with open(output_file + "_desc.txt", "w") as file:
        file.write("\n".join(sorted(cities, reverse=True)))

sort_cities("cities.txt", "sorted_cities")
"""

with open("cities2.txt", "w") as file:
    file.write("LA\nNew York\nTokyo\nDelhi\nParis\nBerlin\nOslo\n")

def count_city_lengths(input_file):
    with open(input_file, "r") as file:
        cities = [city.strip() for city in file.readlines()]  

    print("Character count for each city:")
    length_count = {}  

    for city in cities:
        length = len(city)  
        print(f"{city}: {length} characters")
        length_count[length] = length_count.get(length, 0) + 1

    print("\nCount of cities by length:")
    for length in sorted(length_count): 
        print(f"Length {length} = {length_count[length]} cities")

count_city_lengths("cities2.txt")
