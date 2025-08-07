""" 
Searching algorithms
"""
# Search
def search(S, l, key):
    for i in range(l):
        if(S[i] == key):
            return i
    return -1

print("===================================================")
print("Search")
arr1 = [2,5,7,2,1,7,1,9]
key1 = 7
print(f"Array:{arr1}")
print(f"Key:{key1}")
idx = search(arr1, len(arr1), key1)
print(f"Index of the key in the array: {idx}")

#BinarySearch
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

print("===================================================")
print("BinarySearch")
arr2 = [1,2,3,4,7,9,]
key2 = 7
print(f"Array:{arr2}")
print(f"Key:{key2}")
idx = binarySearch(arr2, len(arr2), key2)
print(f"Index of the key in the array: {idx}")

"""
Sorting algorithms
"""

# SelectionSort
def indexOfMin(S, idx, l):
    minIdx = idx
    while(idx < l):
        if(S[minIdx] > S[idx]):
            minIdx = idx
        idx +=1
    return minIdx
            
def swap(S, idx, minIdx):
    temp = S[idx]
    S[idx] = S[minIdx]
    S[minIdx] = temp
    
def selectionSort(S, l):
    i = 0
    while(i < l):
        minIdx = indexOfMin(S,i,l)
        swap(S,i,minIdx)
        i += 1

print("===================================================")
print("SelectionSort")
arr3 = [2,5,7,2,1,7,1,9]
print(f"Array before sort: {arr3}")
selectionSort(arr3, len(arr3))
print(f"Array after sort: {arr3}")

# InsertionSort
def insertionSort(S, l):
    for nextOne in range(l):
        curr = nextOne
        temp = S[nextOne]
        
        while((curr > 0) and (temp < S[curr - 1])):
            S[curr] = S[curr - 1]
            curr -= 1
        
        S[curr] = temp

print("===================================================")
print("InsertionSort")
arr4 = [2,5,7,2,1,7,1,9]
print(f"Array before sort: {arr4}")
insertionSort(arr4, len(arr4))
print(f"Array after sort: {arr4}")