# A bubble sort is a type of sorting algorithm that sorts sequentially, 
# comparing the first two and swapping them in order of ascending until it reaches the end of the list
# and restarts the whole process over again until all the items are in ascending order


def bubbleSort(myList): # Create a function
    for i in range(0, len(myList) - 1): # This handles the repeated looping / traversal on the list over and over until no more items are swapped
        
        for j in range(0, len(myList) -1): # This controls the indexing iteration of the list
            if myList[j] > myList[j + 1]:   # Compares the preceding item with the succeedng one
                myList[j], myList[j + 1] = myList[j + 1], myList[j] # Then swaps if the above condition returns True
    
    return myList # Return the list after the operation

List1 = [3,4,5,6,45,11,2,1,43,76,32,67,7,8,98,9,49,28]

List2 = ['b', 'd', 'f', 'a', 'c', 'e']


print(bubbleSort(List1))

print()
print()

print(bubbleSort(List2))
