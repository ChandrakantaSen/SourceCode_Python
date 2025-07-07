# Sum of digit of a 3-digit number

n = int(input("Enter the number: "))
a = (n % 10);
b = (n / 10) % 10;
c = (n / 10) / 10;

sum1 = (a + b + c);
print("Sum of Digit: ",int(sum1))
