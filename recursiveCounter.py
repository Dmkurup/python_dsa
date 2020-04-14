def recursive_counter(s):
    #count = 0
    if len(s) ==0:
        return 0
    else:

        return 1+recursive_counter(s[1:  ])

if __name__ == '__main__':
        print(recursive_counter([3,7,9,12]))