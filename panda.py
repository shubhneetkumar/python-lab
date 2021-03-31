num = int(input())

lst = input().split()

lst = list(map(int,lst))

start,Max = num,0

for i in range(num):

   if lst[i] == 1:
   
      start = i
     
      break

X = range(num)

for i in X[num-1::-1]:

  if lst[i] == 1:

     Max = i
  
     break

count = 0

for i in range(start,Max-1):

  if lst[i] == 1:
   
    if lst[i+1] != 1:
  
        count += 1
     
    else:
      
      count += 1

print(count+1)
