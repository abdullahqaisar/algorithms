def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print("Sorted Array: ",arr)
    pass


arr = [1, 20, 51, 2, 9]
bubble_sort(arr)

