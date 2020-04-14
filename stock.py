if len(A)<2:
return -1
i = 0
sell = []
buy = []
n = len(A)
while (i<n-1):
    if="" a[i]="" <="" a[i+1]:=""
    buy.append(i)=""
    while="" (="" i<n-1="" and="" a[i]="" <="" a[i+1]):=
    "" i=+="1"
    if="" len(buy)="=" len(sell)+1:=""
    sell.append(i)="" i="" +="1"
    return="" buy,="" sell="">


    def countOnes(arr, n):
        low = 0
        high = n - 1
        while (low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == 1 and (mid == high or arr[mid + 1] == 0):
                return mid + 1
            elif arr[mid] == 0:
                high = mid - 1
        return 0