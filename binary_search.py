def binary_search(input_array, value):
    length = len(input_array)
    low = 0
    high = length - 1
    
    while (high - low) > 1:
        mid = (high + low) // 2
        if input_array[mid] < value:
            low = mid + 1
        else:
            high = mid
        
    if input_array[high] == value:
        return high
    elif input_array[low] == value:
        return low
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 1
test_val2 = 29
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))