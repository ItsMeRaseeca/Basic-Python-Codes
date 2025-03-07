#WAP to display employee details

class Employee:
    def __init__(self, emp_id, emp_name, gender, city, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.gender = gender
        self.city = city
        self.salary = salary

    def display_emp_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Gender: {self.gender}")
        print(f"City: {self.city}")
        print(f"Salary: {self.salary}\n")

employee1 = Employee(117, "Raseeca Kashelkar", "Female", "Mumbai", 80000)
employee2 = Employee(113, "Carl", "Male", "California", 68000)

employee1.display_emp_details()
employee2.display_emp_details()
