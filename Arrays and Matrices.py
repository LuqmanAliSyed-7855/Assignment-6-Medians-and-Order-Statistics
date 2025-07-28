"""Declaring two classes as Array and Matrix. The Array class defines such simple methods as 
insertion, deletion, access, and display to work with the array. The Matrix class models a two 
dimensional matrix and implements set, get and print methods to set, get and print matrix values. 
In the sample usage, array is used to insert, delete and access elements in the array whereas
the matrix is made, the elements in the matrix are filled and also shown. The two classes apply 
simple list-based implementations to carry out their functions.
"""

# Array implementation

class Array:
    def __init__(self):
        # Initializing an empty array
        self.arr = []

    def insert(self, value, index=None):
        # Inserting a value at a specific index or appending it at the end
        if index is None:
            self.arr.append(value)  
        else:
            self.arr.insert(index, value)  

    def delete(self, index):
        # Deleting the element at the specified index
        if index < len(self.arr):
            self.arr.pop(index)  

    def access(self, index):
        # Accessing the element at a specific index
        if index < len(self.arr):
            return self.arr[index] 
        else:
            return None  

    def display(self):
        # Displaying the current state of the array
        return self.arr


# Example usage
array = Array()
array.insert(10)
array.insert(20)
array.insert(30)
array.insert(40, 1)
array.delete(2)
print(array.access(1))  
print(array.display()) 


# Matrix implementation

class Matrix:
    def __init__(self, rows, cols):
        # Initializing a matrix with given number of rows and columns filled with zeros
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def set_value(self, row, col, value):
        # Setting a value at a specific row and column
        self.matrix[row][col] = value

    def get_value(self, row, col):
        # Getting the value from a specific row and column
        return self.matrix[row][col]

    def display(self):
        # Displaying the matrix in a readable format
        for row in self.matrix:
            print(row)


# Example usage
matrix = Matrix(3, 3)
matrix.set_value(0, 0, 1)
matrix.set_value(1, 1, 2)
matrix.set_value(2, 2, 3)
matrix.display()
