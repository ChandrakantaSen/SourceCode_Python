class Code8:
    n = 0
    def input(self):
        self.n = int(input("Enter the number: "))

    def calculate(self):
        self.input()
        for i in range(1,(self.n+1)):
            if(self.n % i == 0):
                print("Factors are: ",i)
        
obj = Code8()
obj.calculate()