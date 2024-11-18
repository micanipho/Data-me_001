numbers=[1,4,5,6,8]
highest_number=numbers[0]
highest=[]
for i in numbers:
    if i > highest_number:
        highest_number=i
        highest.append(highest_number)
second_largest=highest[-2]
print(second_largest)