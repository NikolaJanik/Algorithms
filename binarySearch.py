def binarySearch(S, l, key):
    left = 0
    right = l - 1
    while(left <= right):
        m = int((left + right)/2)
        if(S[m] == key): 
            return m
        else:
            if(S[m] > key):
                right = m - 1
            else:
                left = m + 1
                
    return -1

arr = [1,2,3,4,7,9,]
key = 7

print("BinarySearch")
print(f"Array:{arr}")
print(f"Key:{key}")

idx = binarySearch(arr, len(arr), key)

print("===================================================")
print(f"Index of the key in the array: {idx}")
