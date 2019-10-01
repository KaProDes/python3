# GCD FOR TWO NUMBERS
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

# GCD FOR TWO NUMBERS
import math
hcf = math.gcd(a, b)

# GCD FOR A LIST
def gcd_list(A):
    res = A[1]
    for c in A[2::]:
        res = gcd(res , c)
    return res

# PRIME CHECKER
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True


t = int(input())
for i in range(t):
	n = list(map(int, input().split(" ")))
	a, b, c = map(int, input().split(" "))
