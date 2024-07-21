
array =[]
sum = 0

for i in range(0,101):
    array.append(i)

for i in array:
    sum += i
result = sum/len(array)
print(result)