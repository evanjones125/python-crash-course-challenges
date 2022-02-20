total = [value for value in range(1, 1_000_001)]

print(min(total))
print(max(total))
print(f"{sum(total)}\n")


for value in range(3, 31, 3):
	print(f"{value}")
print("\n\n")


total = []
for value in range(1, 11):
	value = value ** 3
	total.append(value)
print(total)


#list comprehension version:
total = [value**3 for value in range(1, 11)]
print(f"{total}\n\n")