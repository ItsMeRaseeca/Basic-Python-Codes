name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
education = input("Enter your educational qualification: ")
experience_in_years = int(input("Enter your years of experience: "))

print("\nBIODATA")

if experience_in_years == 0:
    print("Fresher")
elif experience_in_years>=1:
    print("Experienced")

print("Name: " + name)
print("Age: " + age)
print("Gender: " + gender)
print("Educational Qualification: " + education)
print("Years of Experience: " + str(experience_in_years))
