"""
This is a file to do a merge sort on an array. It uses a
recursive algorithm and has a helper function to recombine
after a split. It runs it by creating a random array and applying
the merge sort to print out the sorted array.
"""
import rand
import pdb


def merge_sort(arr):
    """
    This is a recursive function to split the
    array in half repeatedly and then apply the merge sort
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    "Recombines and sorts the two arrays"
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1
            

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    return merge_arr


sample_arr = rand.random_array([None] * 20)
arr_out = merge_sort(sample_arr)

print(arr_out)
