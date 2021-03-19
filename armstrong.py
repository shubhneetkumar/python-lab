#armstrong number
n = input()
ln = len(n)
s = 0
for i in n:
    s += int(i)**ln
if int(n) == s:
    print("no. is armstrong")
else:
    print("no. is not a armstrong")
