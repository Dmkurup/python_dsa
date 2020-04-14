def binarySearch(dataList,target,low,hi):
    if low>hi:
        return False
    else:
        mid = (low+hi)//2
        if dataList[mid]==target:
            return "item found at {}".format(mid)
        elif dataList[mid]>target:
            return binarySearch(dataList,target,low,mid-1)
        else:
            return binarySearch(dataList,target,mid+1,hi)


if __name__=="__main__":
    print(binarySearch([5,7,9,11,15],7,0,4))