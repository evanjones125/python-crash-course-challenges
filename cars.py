cars = ['bmw', 'audi', 'toyota', 'subaru']

#cars.sort(reverse=True)

print("Original list:")
print(cars)

print("\nsorted list:")
print(sorted(cars))

print("\nOriginal list again:")
print(cars)

cars.reverse()
print(f"\n{cars}")

print(f"\n{len(cars)}")