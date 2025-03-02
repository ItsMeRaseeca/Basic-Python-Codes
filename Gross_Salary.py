basic_salary = float(input("Enter the basic salary: "))
grade = input("Enter the grade (A, B, C): ").upper()

if grade == 'A':
    hra = 0.2 * basic_salary
    da = 0.5 * basic_salary
    allowance = 1700
elif grade == 'B':
    hra = 0.2 * basic_salary
    da = 0.5 * basic_salary
    allowance = 1500
else:
    hra = 0.2 * basic_salary
    da = 0.5 * basic_salary
    allowance = 1300

pf = 0.11 * basic_salary

gross_salary = basic_salary + hra + da + allowance - pf

print("The gross salary is: " + str(gross_salary))
