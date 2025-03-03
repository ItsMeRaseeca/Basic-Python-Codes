#WAP to display student grade and result

class StudentDetails:
    def __init__(self, roll_no, name, marks, total_marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.total_marks = total_marks
        self.obtained_marks = sum(self.marks)
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()
        self.result = self.calculate_result()

    def calculate_percentage(self):
        percentage = self.obtained_marks / self.total_marks * 100
        return percentage

    def calculate_grade(self):
        if self.percentage>=90:
            return "A"
        elif self.percentage>=80:
            return "B"
        elif self.percentage>=70:
            return "C"
        elif self.percentage>=60:
            return "D"
        elif self.percentage>=50:
            return "E"
        else:
            return "F"

    def calculate_result(self):
        if self.percentage>=50:
            return "Pass"
        else:
            return "Fail"

    def display_result(self):
        print(f"Student Roll Number: {self.roll_no}")
        print(f"Student Name: {self.name}")
        print(f"Marks Obtained: {self.marks}")
        print(f"Total Marks: {self.total_marks}")
        print(f"Percentage: {self.percentage:.2f}")
        print(f"Grade: {self.grade}")
        print(f"Result: {self.result}")

obt_marks = [94, 89, 92, 92, 84, 88, 91]

stud1 = StudentDetails(143, "Raseeca", obt_marks, 700)
stud1.display_result()
