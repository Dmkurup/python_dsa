def findSmallest(arr):
    smallest=arr[0]
    smallIndex=0
    for i in range(1,len(arr)):
        if arr[i] <smallest:
            smallest=arr[i]
            smallIndex=i
    return smallIndex

def selectionSort(arr):
    newList =[]
    for i in range(0,len(arr)):
        print(arr)
        smallest = findSmallest(arr)
        newList.append(arr.pop(smallest))

    return newList


if __name__ =="__main__":
    print(selectionSort([5,7,4]))