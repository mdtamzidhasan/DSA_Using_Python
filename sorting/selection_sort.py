#The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
my_array=[3, 54, 15, 76, 88, 2, 3, 45]

n=len(my_array)
for i in range(n-1):
    min_index=i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index=j
    min_value=my_array.pop(min_index)
    my_array.insert(i,min_value)

print('Selection sort: ',my_array)

#Imporved selection sort because shifting is a problem so that the solution is swap.

my_aray=[45, 54, 15, 76, 88, 11, 3, 45]

n=len(my_aray)
for i in range(n-1):
    min_index=i
    for j in range(i+1, n):
        if my_aray[j] < my_aray[min_index]:
            min_index=j
    my_aray[i],my_aray[min_index]=my_aray[min_index],my_aray[i]

print('Improved Selection sort: ',my_aray)