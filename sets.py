numbers = {1, 2, 3, 4}
# print(numbers)

#numbers = ([1, 2, 2, 3])
#print(numbers)

#add numbers to the set
numbers.add(8)
print(numbers)

names = set(['Alice', 'Bob', 'Charlie', 'Alice'])
names.add('Zama')
names.remove('Bob')
print(f'Original set: {names}')

#union of set operations
print(names|numbers)   #combining sets
