#WAP to check whether no. is prime number and armstrong number

class CheckNumber:

    def __init__(self, num):
        self.num = num
    
    def is_Prime(self):
        if self.num<2:
            return False

        for i in range(2, int(self.num**0.5)+1):
            if self.num%i == 0:
                return False

        return True

    def is_Armstrong(self):
        
        order = len(str(self.num))

        total = 0

        temp = self.num
        while temp>0:
            digit = temp%10
            total += digit**order
            temp //= 10

        if total == self.num:
            return True
        else:
            return False

    def display_result(self):
        if self.is_Prime():
            print("Prime Number")
        else:
            print("Not a Prime Number")

        if self.is_Armstrong():
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

num1 = int(input("Enter a number: "))
number1 = CheckNumber(num1)
number1.display_result()
