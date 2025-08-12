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

# MergeSort
def merge(a1, len1, a2, len2):
    i = 0
    j = 0
    k = 0
    result = [0] * (len1 + len2)
    
    while((i < len1) and (j < len2)):
        if(a1[i] < a2[j]):
            result[k] = a1[i]
            k += 1
            i += 1
        else:
            result[k] = a2[j]
            k += 1
            j += 1
            
    while(i < len1):
        result[k] = a1[i]
        k += 1
        i += 1
        
    while(j < len2):
        result[k] = a2[j]
        k += 1
        j += 1
    return result

def mergeSort(S, l):
    if(l <= 1):
        return S[0:l]
    m = int(l/2)
    return merge(mergeSort(S[0:m], m), m,
                 mergeSort(S[m:l], l-m), l-m)

print("===================================================")
print("MergeSort")
arr5 = [2,5,7,2,1,7,1,9]
print(f"Array before sort: {arr5}")
arr5Sorted = mergeSort(arr5, len(arr5))
print(f"Array after sort: {arr5Sorted}")


#QuickSort
def partition(a, left, right):
    i = left + 1
    j = right
    p = a[left] #pivot
    
    while(True):
        while((i < right) and (a[i] <= p)):
            i +=1
        while((j > i) and (a[j] >= p)) :
            j -=1
        if(i < j):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
        if(i<j):
            continue
        else:
            break
        
    if(a[i] > p):
        a[left] = a[i-1]
        a[i-1] = p
        return i-1
    else:
        a[left] = a[i]
        a[i] = p
        return i


