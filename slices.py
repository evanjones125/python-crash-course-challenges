my_vars = ['x', 'y', 'z', 'a', 'b']
friend_vars = my_vars[:]

my_vars.append('c')
friend_vars.append('d')

print("First three vars:")
for var in my_vars[:3]:
	print(var)

print(f"\n{my_vars}")
print(f"\n{friend_vars}")