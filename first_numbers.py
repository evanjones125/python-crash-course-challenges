#for value in range(1, 5):
#	print(value)

#odd_numbers = list(range(1, 11, 3))
#print(odd_numbers)


#creates a list of the first  10 square numbers

squares = []
for value in range(1, 11):
	#square = value ** 2
	squares.append(value ** 2)
	
print(squares)
#print(f"{sum(squares)}\n\n")


#list comprehension doing same function as above
squares = [value**2 for value in range(1, 11)]
print(squares)