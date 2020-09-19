def swap(arr, x ,y):
    arr[x] += arr[y]
    arr[y] = arr[x]-arr[y]
    arr[x] -= arr[y]

def compare_and_swap(arr, index, size):
    largest = index
    l = index*2 + 1
    r = index*2 + 2

    if r < size and arr[r] > arr[largest]:
        largest = r

    if l < size and arr[l] > arr[largest]:
        largest = l
    
    #if a swap is done then all sub trees below this must be checked again 
    if largest != index:
        swap(arr, index, largest)
        compare_and_swap(arr, largest, size)


def heapify(arr, index, size):
    #start from the level (height - 1) i.e. last level of non-leaf nodes
    last_parent = int(len(arr)/2) - 1
    for i in range(last_parent , -1, -1):
        compare_and_swap(arr, i, size)


if __name__ == "__main__":
    n = int(input("Enter number of integers : "))
    arr = [ int(input("Enter number %d : " % (i+1))) for i in range(n)]
    heapify(arr, 0, len(arr))
    print(arr)
