#water tank problem
r = 5
h= 10
f = 10
t = input("Enter the time")

vtank = 3.14*r**2*h
vwtr = f*t

if vwtr>vtank:
    print("over flow condition")
    print("volume of",vwtr-vtank)
elif vwtr ==vtank:
    print("Tank full")

else:
    print("underflow condition")
    ht = vwtr/(3.14*r**2)
    hr = h-ht
    print(f"filled height{ht}\n remaining height {hr})
