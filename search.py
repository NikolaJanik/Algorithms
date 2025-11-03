def search(S, l, key):
    for i in range(l):
        if(S[i] == key):
            return i
    return -1


arr = [2,5,7,2,1,7,1,9]
key = 7
print("Search")
print(f"Array:{arr}")
print(f"Key:{key}")
idx = search(arr, len(arr), key)
print("===================================================")
print(f"Index of the key in the array: {idx}")
