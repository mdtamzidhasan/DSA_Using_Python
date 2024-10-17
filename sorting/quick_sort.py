#As the name suggests, Quicksort is one of the fastest sorting algorithms.
#The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that lower values are on the left of the pivot element, and higher values are on the right of it.

def partision(array,low,high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j]<=pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high],array[i+1]
    return i+1


def quickSort(array, low=0, high=None):
    if high is None:
        high=len(array)-1

    if low <= high:
        pivot_index=partision(array,low,high)
        quickSort(array,low,pivot_index-1)
        quickSort(array,pivot_index+1,high)






my_array=[22,33,55,66,88,44,22,4]
quickSort(my_array)
print("Quick sort: ", my_array)