# TO-DO: complete the helper function below to merge 2 sorted arrays

import math
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    new_arr = []
    index_a = 0
    index_b = 0
    while len(new_arr) < len(merged_arr):
      if len(arrA) == index_a:
        return new_arr + arrB[index_b:]
      if len(arrB) == index_b:
        return new_arr + arrA[index_a:]
      if arrA[index_a] <= arrB[index_b]:
        new_arr.append(arrA[index_a])
        index_a += 1
      else:
        new_arr.append(arrB[index_b])
        index_b +=1
    
    return merged_arr

print("TEST", merge([1,2,8], [3,5,7]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
      sub1 = []
      sub2 = []
      midpoint = math.floor(len(arr) / 2)
      sub1 = arr[:midpoint]
      sub2 = arr[midpoint:]
      print(sub1)
      print(sub2)
      sorted1 = merge_sort(sub1)
      sorted2 = merge_sort(sub2)
      print(sorted1)
      print(sorted2)
      arr = merge(sorted1, sorted2)
    return arr


arr1 = [1, 2, 3]
# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]




# merged = merge_sort(arr1)
# print(merged)



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
