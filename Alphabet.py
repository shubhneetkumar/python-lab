import re
your_string = input("Enter the string")
result = re.sub('[\d\W_]+', '', your_string)  
print ("Your final string is : ", result)
