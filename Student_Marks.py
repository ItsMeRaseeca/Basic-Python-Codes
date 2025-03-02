num_subjects = int(input("Enter the number of subjects (3 or 5): "))

if num_subjects == 3 or num_subjects == 5:
    total_marks = 0
    for i in range(1, num_subjects + 1):
        print("Enter marks for subject " + str(i) + ": ", end="")
        marks = float(input())
        total_marks += marks

    percentage = (total_marks / (num_subjects * 100)) * 100

    print("The total marks are: " + str(total_marks))
    print("The percentage is: " + str(percentage) + "%")
else:
    print("Invalid number of subjects! Please enter either 3 or 5.")
