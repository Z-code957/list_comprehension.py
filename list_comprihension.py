numbers = []
for i in range(10):
    num = int(input("Enter a positive number: "))
    numbers.append(num)
print(numbers)
numbers = [int(input("Enter a positive number: ")) for i in range(10)]
print("Total list of numbers: ", numbers)
even = [x for x in numbers if x%2==0]
print(even)
odd = [x for x in numbers if x%2!=0]
print(odd)
