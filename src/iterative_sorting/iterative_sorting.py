# Insertion sort from guided demo
def insertion_sort(array):
    # create loop that goes from the 1st index to last
    for i in range(1, len(array)):
        print(array)
        #  Consider element at index 0 to be our sorted piece. The rest of the array is our unsorted piece.
        # Save the 1st element in the unsorted piece in a temp variable.
        temp = array[i]
        # iterator for second loop
        # j will count downward
        j = i
        # while j is greater than 0 and our temp variable is smaller
        while j > 0 and temp < array[j - 1]:
            # Shift elements in the sorted piece over to the right until we find where the element from step 2 should go.
            # shift left until correct position is found
            array[j] = array[j - 1]
            # increment down
            j -= 1
        # Insert the element from step 2 into its correct index within the sorted piece.
        array[j] = temp
        # Repeat steps 2-4 until all elements have been processed.
    return array

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr