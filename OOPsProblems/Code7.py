class Code7:
    n = 0
    def input(self):
        self.n = int(input("Enter the number: "))

    def calculate(self):
        self.input()
        fact = 1
        for i in range(1,(self.n+1)):
            fact = fact*i

        print("Factorial Value is: ",fact)
        
obj = Code7()
obj.calculate()