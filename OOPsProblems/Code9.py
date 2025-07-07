class Code6:
    a = b = 0
    def input(self):
        self.a = int(input("Enter the length: "))
        self.b = int(input("Enter the breadth: "))

    def calculate(self,x,y):
        area = (x*y)
        perimeter = 2*(x+y)

        print("Area is: ",area)
        print("Perimeter is: ",perimeter)

    def display(self):
        self.input() 
        self.calculate(self.a,self.b)

obj = Code6()
obj.display()