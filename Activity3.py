class expressions:
    def __init__(self , num1 , num2 , num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
    
    def addition(self):
        add=self.num1+self.num2+self.num3
        print(f"The addition of values {self.num1} , {self.num2} , {self.num3} is {add}")

obj=expressions(78 , 56 , 62)
obj.addition()
