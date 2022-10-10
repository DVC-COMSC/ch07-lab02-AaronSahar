import random
numbers = []
for i in range(10):
    numbers.append(random.randint(0, 100))
smallest = int(min(numbers))
index_number = numbers.index(smallest)
print(smallest)
print(index_number)