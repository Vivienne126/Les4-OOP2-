class expressions:
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    def addition(self):
        add=self.num1+self.num2+self.num3
        print(f"Ans of addition: {add}")
    def subtract(self):
        sub=self.num1-self.num2-self.num3
        print(f"Ans of subtraction: {sub}")
    def multiply(self):
        mul=self.num1*self.num2*self.num3
        print(f"Ans of multiplication: {mul}")
    def divide(self):
        div=self.num1/self.num2/self.num3
        print(f"Ans of division: {div}")

a=int(input("Enter number"))
b=int(input("Enter number"))
c=int(input("Enter number"))

obj=expressions(a , b , c)
print(f"Addition of {a} , {b} , {c} = {obj.addition()}")
print(f"Subtraction of {a} , {b} , {c} = {obj.subtract()}")
print(f"Multiply of {a} , {b} , {c} = {obj.multiply()}")
print(f"Divide of {a} , {b} , {c} = {obj.divide()}")

