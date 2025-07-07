class Code6:
    a = b = 0
    def input(self):
        self.a = int(input("Enter the number 1: "))
        self.b = int(input("Enter the number 2: "))

    def calculate(self,x,y):
        return (x+y)

    def display(self):
        self.input() 
        p = self.calculate(self.a,self.b)
        print("Sum is: ",p)

obj = Code6()
obj.display()