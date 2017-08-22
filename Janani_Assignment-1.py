		""" Python course: Assignment-1 
    			Date : 22/08/2017 """


# Create a list with the first ten triangular numbers
L = [(i*(i+1)/2) for i in range(10)]
print L

		##### OUTPUT #####
#[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

# Program to check if a number is prime or not
def is_prime(n):
    lm = list()
    for i in range(2,n):
        lm.append(n%i)
    if 0 in lm:
        return False
    else:
        return True
        

		##### OUTPUT #####
is_prime(625)
#False

is_prime(2039)
#True
      
''' while calling the function using is_prime(n), example: is_prime(7) will output True if it is a prime, else False '''

# Printing next 10 prime numbers
def next_ten_primes(n):
    ls=list()
    while n>1:
        if is_prime(n):
            ls.append(n)
            n=n+1
            if len(ls)==10:
                break
        else:
            n=n+1
    return ls

		##### OUTPUT #####
next_ten_primes(2039)
#[2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]

next_ten_primes(3500)
#[3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559]


