my_array=[3, 22, 66, 2, 5, 33, 22]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]


print('sorted array: ',my_array)

