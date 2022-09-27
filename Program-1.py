#Problem1
#Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    #Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    #Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

#creating calculator class for different operaations
class Calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        return self.a+self.b
    def sub(self,a,b):
        return self.a-self.b
    def mul(self,a,b):
        return self.a*self.b
    def div(self,a,b):
        return self.a/self.b
    def add(self,a,b):
        return self.a+self.b

#Taking input from user    

a=float(input("a="))
b=float(input("b="))

#creating object of class Calc
c=Calc(a,b)

operator=str(input("type of operation="))
if operator=="+":
    print(a,"+",b,"=",c.add(a,b))
elif operator=="-":
    print(a,"-",b,"=",c.sub(a,b))
elif operator=="*":
    print(a,"*",b,"=",c.mul(a,b))
elif operator=="/":
    print(a,"/",b,"=",c.div(a,b))
else:
        print("Invalid Operator!!")
  
   
