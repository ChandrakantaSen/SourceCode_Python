class highlow:
    m=n=0
    def input(self):
        self.m=int(input(" enter the 1st number "))
        self.n=int(input(" enter the 2nd number "))
        
    def calculate(self,m,n):
        p=m*n
        i=1
        while(i<p):
            if(m%i==0 and n%i==0):
                h=i
            i=i+1
        l=int(p/h)
        print(" hcf is",h)
        print(" lcm is ",l)
        
    def display(self):
        self.input()
        self.calculate(self.m,self.n)
        
obj=highlow()
obj.display()