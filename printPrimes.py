import math


def printPrimes(n):
    primes =[i for i in range(2,n+1)]

    p=2
    while p <= int(math.sqrt(n)):
       if p in primes:
          for j in range(p*p, n+1,p):
             if j in primes:
               primes.remove(j)
       p+=1
    return primes









if __name__ == '__main__':
        print(printPrimes(10))