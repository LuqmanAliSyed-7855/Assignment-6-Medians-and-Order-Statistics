"""The Randomized Quick Select algorithm has been implemented that is utilized to establish 
the k-th smallest element in an unorganized array. The array is divided at a randomly chosen 
pivot, and the process is repeated until the required element is located. The partition function
will make sure that smaller elements than the pivot are to the left and the larger ones are 
to the right. The algorithm is tested by determining the 4th smallest element of an example 
array, proving the effectiveness of this method when choosing order statistics."""

# Importing necessary libraries
import random

# Function to perform the partition step of the quickselect algorithm
def partition(arr, low, high):
    # Setting the pivot to be the last element
    pivot = arr[high]
    i = low - 1
    # Looping through the array to arrange elements around the pivot
    for j in range(low, high):
        # Swapping elements smaller than pivot to the left side
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Swapping pivot with the element at the partition point
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to perform the partition step of the quickselect algorithm 
def randomized_partition(arr, low, high):
    # Selecting a random pivot index between low and high
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  
    return partition(arr, low, high) 

# Function to select the k-th smallest element using randomized quickselect
def randomized_quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]  
    
    low, high = 0, len(arr) - 1
    # Looping to partition and select the correct k-th smallest element
    while low <= high:
        pivot_index = randomized_partition(arr, low, high)  
        if pivot_index == k:
            return arr[pivot_index]  
        elif pivot_index < k:
            low = pivot_index + 1  
        else:
            high = pivot_index - 1  

# Example to test randomized_quickselect
arr = [12, 3, 5, 7, 19, 2]
k = 4  # Looking for the 4th smallest element
result = randomized_quickselect(arr, k - 1)  
print(f"4th smallest element (using Randomized Quickselect) is: {result}")
