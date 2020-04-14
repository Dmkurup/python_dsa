def maxList(s):
  if len(s)==2:
      return s[0] if s[0]>s[1] else s[1]
  subMax=maxList(s[1:])
  return s[0] if s[0]>subMax else subMax

if __name__ == '__main__':
        print(maxList([3,7,9,12]))