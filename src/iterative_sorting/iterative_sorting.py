# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for s in range(cur_index, len(arr)):
            if arr[s] < arr[smallest_index]:
                arr[smallest_index], arr[s] = arr[s], arr[smallest_index]
    return arr
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# sorted = selection_sort(arr1)
# print(sorted)

        # TO-DO: swap


# loop twice - 2 for loops, one for current index and 1 for smallest index
    # if cur_index > smallest index, swap indexes
    # if not leave in the same spot
    # return arr
    

# loop twice, once for current index, one for current index +1
# if current index > next index, swap spots
# if not leave it
# current index becomes current + 1, compares to the next one




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    didSwap = True
    while didSwap:
        didSwap = False
        for i in range(0, len(arr) -1):
            cur_index = i
            next_index = i + 1
            if arr[cur_index] > arr[next_index]:
                arr[cur_index], arr[next_index] = arr[next_index], arr[cur_index]
                didSwap = True
                
    return arr



# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#     #   [5, 8, 4, 2, 9, 6, 1, 3, 7, 0]
# bubbleSorted = bubble_sort(arr1)
# print(bubbleSorted)








# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr