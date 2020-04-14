def find_MaxMin(data, l, r):
    mid = (l + r) // 2
    if l == mid:
        return min(data[l], data[r]), max(data[l], data[r])
    else:
        lmin, lmax = find_MaxMin(data, l, mid)
        rmin, rmax = find_MaxMin(data, mid, r)
        return min(lmin, rmin), max(lmax, rmax)

if __name__ == '__main__':
        print(find_MaxMin([3,7,9,12],0,3))