""" a py program using class which contains maths methods of """
# multiplication table
# square
# cube
# square root
# prime number
# Fibonnaci sequence
# Factorial of number
# Sum of give n natural number
class maths():

    def __init__(self,num):
        self.num = num
        print(f"The given number is {self.num}")

    def multi_table(self):  
        for i in range(1,11):
            if i==10:
                print(f"{self.num}x{i}= {self.num*i}")
            else:        
                print(f"{self.num}x{i} = {self.num*i}")
        print("__________")

    def square(self):
        print(f"The square of the given number {self.num} is {self.num**2}")

    def cube(self):
        print(f"Cube of given number {self.num} is {self.num**3}")

    def square_root(self):
        print(f"Square root of given number {self.num} is {int(self.num**0.5)}")

    def prim_number(self):
        pn = f"{self.num} is a prime number"
        np = f"{self.num} is not a prime number"
        if self.num == 0 or self.num == 1:
            print(np)
        else: 
            for i in range(2,self.num):
                if self.num%i == 0:
                    print(np)
                    break
            else:
                print(pn)
    @staticmethod
    def fibo_num(num):
        def fib(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return    fib(num-1)+fib(num-2)
        print(fib(num))
    @staticmethod
    def factorial(num):
        def fact(num):    
            if num == 0 or num ==1:
                return 1
            else:
                return num*fact(num-1)
        print(fact(num))
    
    @staticmethod
    def sum_natural(num):
        def sumn(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return num+sumn(num-1)
        print(sumn(num))             

# call = maths(num = int(input("Enter a number\nHere....")))
# call.square_root()
message = "Enter a number to execute the operation\nHere...."
def fun():
    
    global message
    print("\nMulti = Multiplication Table,\nS = Square of a Number\nCU = Cube Value\nSR = Square Root\nPN = Prime Number\nFS = Fibonnaci Sequence\nFV = Factorial Value\nSN = Sum of Natural number")
    
    while 1:
        opr = (input("*****************************\nSelect the keyword to proceed or\nenter 'c' to continue, 'e' to exit\nHere>> \n")).upper()
        
        if opr == 'C':
            fun()
        elif opr == "E":
            print("Thank you for four Valuable time\n______Have a nice day______")
            break
        elif opr == "M":
            call = maths(num = int(input(message)))
            call.multi_table()
        elif opr == "S":
            call = maths(num = int(input(message)))
            call.square()
        elif opr == "CU":
            call = maths(num = int(input(message)))
            call.cube()
        elif opr =="SR":
            call = maths(num = int(input(message)))
            call.square_root()
        elif opr =="PN":
            call = maths(num = int(input(message)))
            call.prim_number()
        elif opr =="FS":
            call = maths(num = int(input(message)))
            call.fibo_num(call.num)
        elif opr =="FV":
            call = maths(num = int(input(message)))
            call.factorial(call.num)
        elif opr=="SN":
            call = maths(num = int(input(message)))
            call.sum_natural(call.num)
        else:
            print("Invalid litteral,try again\n")
fun()

"""__________________________________THE_END____________________________________"""