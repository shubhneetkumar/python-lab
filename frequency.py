strA = input("Enter a string")
res = {}
for keys in strA:

    res[keys] = res.get(keys, 0) + 1

print("Frequency of each character : \n",res)
