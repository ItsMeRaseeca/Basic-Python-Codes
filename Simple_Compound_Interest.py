principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

if principal > 0 and rate_of_interest > 0 and time > 0:
    simple_interest = (principal * rate_of_interest * time) / 100

    compound_interest = principal * (1 + rate_of_interest / 100) ** time - principal

    print("The Simple Interest is: " + str(simple_interest))
    print("The Compound Interest is: " + str(compound_interest))
else:
    print("Please enter valid positive values for principal, rate of interest, and time.")
