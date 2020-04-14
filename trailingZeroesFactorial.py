def findTrailingZeroes(n):
    i=5
    count=0
    while n/i>=1:
        count+=int(n/i)
        i*=5
    return count


if __name__ == '__main__':
    print(findTrailingZeroes(20))