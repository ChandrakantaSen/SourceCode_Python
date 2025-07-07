class Code4:
    n = 0
    def input(self):
        self.n = int(input("Enter the number: "))

    def display(self):
        self.input()
        print("Value is: ", self.n)

obj = Code4()
obj.display()
