def merge_sorted_arrays(arr1, arr2):
    result = arr1 + arr2
    result.sort()
    return result
    

def merge_sorted_arrays2(arr1, arr2):
    my_list = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            my_list.append(arr1[i])
            i += 1
        elif arr2[j] <= arr1[i]:
            my_list.append(arr2[j])
            j += 1
    return my_list + arr1[i:] + arr2[j:]


array1 = [1, 2, 5, 8, 31, 70, 0]
array2 = [3, 0, 6, 8, 20, 66]

print(merge_sorted_arrays2(array1, array2))
