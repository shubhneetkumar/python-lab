def sortLexo(my_string):

	
	words = my_string.split()
	
	
	words.sort()

	
	for i in words:
		print( i )


if __name__ == '__main__':
	
	my_string = input("Enter the string : ")
			
	
	sortLexo(my_string)
