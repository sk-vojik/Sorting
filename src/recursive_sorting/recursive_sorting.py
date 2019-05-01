from time import time

import random

l = [random.randint(0,1000) for i in range(0,100)]

print(l)

def merge(arrA, arrB):

  elements = len(arrA) + len(arrB)
  merged_arr = [0] * elements

  a = 0
  b = 0

    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
  for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
  return merged_arr


def merge_sort(arr):
# 1. While your data set contains more than one item, split it in half
  if (len(arr) > 1):
    left = merge_sort(arr[0: int(len(arr)/2)])
    right = merge_sort(arr[int(len(arr)/2):])
# 2. Once you have gotten down to a single element, you have also *sorted* that element 
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
    arr = merge(left, right)  # haven't defined merge is? 
# 4. Repeat step 3 until the entire data set has been reassembled
  return arr
    



# Algorithm to time our code

# Store a startin time
start_time = time()

# Run our code
merge_sort(l)
print(l)

# Store the ending time
end_time = time()

print (end_time - start_time)


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
