# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    # TO-DO

    while arrA and arrB:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))

    if arrA:
        merged_arr = merged_arr + arrA
    if arrB:
        merged_arr = merged_arr + arrB

    return merged_arr


# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO
#     a = 0
#     b = 0
#     # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
#     for i in range(0, elements):
#         if a >= len(arrA):    # all elements in arrA have been merged
#             merged_arr[i] = arrB[b]
#             b += 1
#         elif b >= len(arrB):  # all elements in arrB have been merged
#             merged_arr[i] = arrA[a]
#             a += 1
#         elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
#             merged_arr[i] = arrA[a]
#             a += 1
#         else:  # else, next element in arrB must be smaller, so add it to final array
#             merged_arr[i] = arrB[b]
#             b += 1
#     return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        return merge(merge_sort(arr[:len(arr)//2]),
                     merge_sort(arr[len(arr)//2:]))
    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
