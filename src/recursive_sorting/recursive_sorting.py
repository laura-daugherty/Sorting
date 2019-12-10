# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr



arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]



merged = merge_sort(arr1)
print(merged)



# # Step 1: split into smaller lists
# [5 9 3 7 2 8 1 6]
# [5 9 3 7] [2 8 1 6]
# [5 9] [3 7] [2 8] [1 6]
# [5] [9] [3] [7] [2] [8] [1] [6]
# # Step 2: merge
# [5] [9] [3] [7] [2] [8] [1] [6]
# [5 9] [3 7] [2 8] [1 6]
# [3 5 7 9] [1 2 6 8]
# [1 2 3 5 6 7 8 9]
# To merge, walk along the two lists with two different indexes, and move the
# smaller number into the destination list and advance that list's index. Repeat
# until both lists are empty.











# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
