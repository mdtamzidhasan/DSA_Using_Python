my_array=[3, 22, 66, 2, 5, 33, 22]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]


print('sorted array: ',my_array)

#Bubble sort improved
#If it is already sorted, then we don't need to use any algorithm.

n = len(my_array)
for i in range(n-1):
    swaped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
            swaped = True
    if not swaped:
        break


print('sorted array: ',my_array)

#the time complexity for Bubble Sort is: O(n)^2