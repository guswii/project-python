#sudarsana program
def LinearSearch(array, n, k):
    
    for j in range(0, n):
        
        if (array[j] == k):
            return j
    return -1

array = [1, 3, 5, 7, 9]

k = 3
n = len(array)

result = LinearSearch(array, n, k)

if(result == -1):
    
    print("DATA TIDAK DITEMUKAN")
    
else:
    
    print("DATA DITEMUKAN pada index: ", result)