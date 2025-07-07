class Code5:
    def __init__(self):
        self.n = 0

    def input(self):
        self.n = int(input("Enter the number: "))

    def display(self):
        print("Value is: ", self.n)

obj = Code5()
obj.input()
obj.display()