#anagram string
s1 = input("Enter first string:")
s2 = input("Enter second string:")

if(sorted(s1) == sorted(s2)):
    print("string are anagram")
  
else:
    print("strings are not anagram")
