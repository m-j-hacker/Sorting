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
    # First, we need to loop through the array
    while not swapped:

        for i in range(1, len(arr)):
        # Then, we need to compare each element to the one next to it
        # If arr[i-1] > arr[i], perform our swap
            cur_index = i
            print(cur_index)
            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                swapped = True
                break
    
    return arr

bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr