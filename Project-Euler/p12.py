# The sequence of triangle numbers is generated by adding the natural numbers. So the 7^(th) triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

# LOGIC:
# Generate all the prime numbers till sqrt(num) + 1
# find the prime factors of the numbers
# use the formulae multiple of (exponents + 1)

import math

## can add an optimization by *memoizing* factors
def nextPrime(list, it):
    while True:
        next_num = it.next() 
        flag = 0
        sqrt = next_num ** .5
        for i in list:
            if next_num % i == 0:
                flag = 1
                break
            if sqrt < i:
                flag = 0
                break
        if flag: continue
        else: return next_num


def naturalNumbers(init):
    counter = init

    while True:
        yield counter
        counter += 1

## only array method works
def seqTriangle():
    counter = [0]

    def _closure(next):
        counter[0] += next
        return counter[0]

    return _closure


# LOGIC:
# If you factor a number into its prime power factors, then the total
# number of factors is found by adding one to all the exponents and
# multiplying those results together. Example: 108 = 2^2*3^3, so the 
# total number of factors is (2+1)*(3+1) = 3*4 = 12. Sure enough, the
# factors of 108 are 1, 2, 3, 4, 6, 9, 12, 18, 27, 36, 54, and 108.

def numFactors(num, primes):
    factors = []
    counter = 0
    count = 1
    flag = 0
    if num == 1: return 1
    while num > 1:
        if num % primes[counter] == 0:

            if flag: factors[-1] += 1
            else: factors.append(1)
            
            num /= primes[counter]
            flag = 1
            ## if num is prime, no more divisions are possible 
            ## also make sure, this prime number is not the current prime number
            ## else exponents will get screwed (ie, 9 = 3 * 3, so factors should contain 2, not 1, 1)
            if num > 1 and num != primes[counter] and isPrime(num):
                factors.append(1)
                break
        else:
            flag = 0
            counter += 1

    return reduce(lambda x,y: (x) * (y), map(lambda x: x + 1, factors))

def isPrime(num):
    if num == 1 or num == 2:
        return True
    
    ## even numbers
    if not num & 1:
        return False

    for x in range(3, int(num**0.5)+1, 2):
        if num % x == 0:
            return False

    return True

if __name__ == '__main__':
    nums  = naturalNumbers(1)
    seq_f = seqTriangle()
    primes = [2,]
    it = naturalNumbers(2)

    while True:
        tri_num = seq_f(nums.next())

        while (math.ceil(tri_num ** .5) + 1 >  primes[-1]):
            next_prime = nextPrime(primes, it)
            primes.append(next_prime)

        if numFactors(tri_num, primes) >= 500:
            print tri_num, numFactors(tri_num, primes)
            break
            

