
def merge_sort(arr):
    if (len(arr) > 1):

        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        if (i < len(L)) and (j < len(R)):
            pass


arr = [1, 20, 51, 2, 9, 10]
merge_sort(arr)


# arr = [100, 20, 51, 2, 9, 10]

# L=[100, 20, 51]                   R=[2, 9, 10]

# L=[100]  R=[20, 51]               L=[2]      R=[9, 10]

#        L=[20] R=[51]                     L=[9] R=[10]

# L=[100]  R=[20, 51]               L=[2]      R=[9, 10]

# L=[100, 20, 51]                   R=[2, 9, 10]

# arr = [100, 20, 51, 2, 9, 10]
