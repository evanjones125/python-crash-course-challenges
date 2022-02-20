#looping through a slice with a for loop
#iterates through list slicepractice at positions
#x:y and cubes the values

slicepractice = [4, 1, 6, 5, 8, 9, 1, 7]

for slicevar in slicepractice[2:5]:
	slicevar = slicevar ** 4
	print(slicevar)