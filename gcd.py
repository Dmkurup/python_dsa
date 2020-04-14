def gcd(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(2, small + 1):
        if num1 % i == 0 & num2 % i == 0:
            return i


if __name__ == "__main__":
    in_str = input("Enter numbers:")
    numList = [int(val) for val in in_str.split()]
    print("GCD FOR {},{} IS {}".format(numList[0], numList[1], gcd(numList[0], numList[1])))
