class Code6:
    a = b = 0
    def input(self):
        self.a = int(input("Enter the number_1: "))
        self.b = int(input("Enter the number_2: "))

    def calculate(self,x,y):
        if(x > y):
            print("Maximum is: ",x)
        else:
            print("Maximum is: ",y)

    def display(self):
        self.input() 
        self.calculate(self.a,self.b)

obj = Code6()
obj.display()