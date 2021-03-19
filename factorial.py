#factorial of number
fact = 1
X = int(input("Enter a number"))
for i in range(1,X+1):
    fact = fact*i
print("factorial is",fact)
