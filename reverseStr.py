# def reverse_str(s):
# #     if len(s) >= 2:
# #         innerReversed = reverse_str(s[1:-1])
# #         innerReversed.append(s[0])
# #         innerReversed.insert(0, s[-1])
# #         return innerReversed
# #     else:
# #         return list(s)


def reverse_str(s,start,stop):
    if start >stop-1:
        return s
    elif start==stop:
        return s[start]

    elif   start <=stop-1:
        s[start],s[stop-1]=s[stop-1],s[start]
        reverse_str(s,start+1,stop-1)


if __name__ == '__main__':
    print(reverse_str('pots&pans',0,9))