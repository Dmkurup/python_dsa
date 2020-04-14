def isPalindrome(s):
    if len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            return isPalindrome(s[1:-1])
    else:
        return True

if __name__ == '__main__':
        print(isPalindrome('racecar'))


# def palindrome(s):
#     if len(s) > 1:
#         if s[0] != s[-1]:
#             return False
#         else:
#             return palindrome(s[1:-1])
#     else:
#         return True
#
# if __name__ == '__main__':
#     print(palindrome('racecar'))
#     print(palindrome('gohangasalamiimalasagnahog'))