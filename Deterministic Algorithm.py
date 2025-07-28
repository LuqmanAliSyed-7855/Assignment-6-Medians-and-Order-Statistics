"""Using the Median of Medians algorithm to choose the k-th element of an unordered array of 
numbers. It splits the array into roughly two parts around a pivot, and then recursively selects 
a median of medians used as a pivot for efficient selection. The algorithm also has worst-case 
linear time. In the example, it finds the 4th smallest element by calling the deterministic_select 
function with a sample array, demonstrating how the algorithm works for selecting order statistics."""


# Importing necessary library
import math

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

# Function to find the median of a list by sorting
def find_median(arr):
    arr.sort()  # Sorting the list
    return arr[len(arr) // 2]  

# Function to partition the list into groups of five and find their medians
def median_of_medians(arr):
    # Splitting the array into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    
    # Finding the median of each group
    medians = [find_median(group) for group in groups]
    
    # Recursively finding the median of medians if necessary
    if len(medians) <= 5:
        return find_median(medians)
    
    return median_of_medians(medians)

# Function to select the k-th smallest element
def deterministic_select(arr, k):
    if len(arr) == 1:
        return arr[0]  
    
    pivot = median_of_medians(arr) 
    low, high = 0, len(arr) - 1
    
    # Looping to partition and select the correct k-th smallest element
    while low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]  
        elif pivot_index < k:
            low = pivot_index + 1  
        else:
            high = pivot_index - 1 

# Example to test deterministic_select
arr = [12, 3, 3, 7, 19, 2]
k = 4  # Looking for the 4th smallest element
result = deterministic_select(arr, k - 1)  
print(f"4th smallest element is: {result}")
