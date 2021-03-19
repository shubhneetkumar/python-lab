#fibonacci sequence up to nth term
n = int(input("Enter a value"))
n1,n2 = 0,1
count = 0
if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print("fibonnaci sequence upto",n,":")
    print(n1)
else:
    print("fibonnaci sequence:")
    while count < n:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1
              
