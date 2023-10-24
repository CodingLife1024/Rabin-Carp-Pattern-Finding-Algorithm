import random
import math

#To generate a hash function as - [?, A, B, C, D, E, F....] = [0, 0, 1, 2, 3, 4, 5]
def hash(letter): 
    if letter == "?":
        return 0
    return ord(letter) - 65

# Implements the horners function to improve the time complexity of the code
def horner(st):
    #To list out the hash functions of all the characters in the given string
    poly = [hash(st[i]) for i in range(len(st))] 
    res = 0
    for i in range(len(st)):
        res = res*26 + poly[i]
    return res

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
    return math.ceil(((m/eps)*math.log(26,2))**2)

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
    M = len(p)
    N = len(x)
    o = 26**(M-1) #This is stored to improve the time complexity of the code
    a = horner(p)
    b = horner(x[0:M])
    l = []
    for i in range(N-M+1):
        if a%q == b%q:
            l.append(i)
        if i < N-M:
            #This new b is the hash function of the next block of text of length M in the string x.
            # It removes the first character and adds the immidiate next character of the substring to generate a new b.
            b = ((26*(b - (o*hash(x[i]))) + (hash(x[i+M])))%q + q)%q 
    return l

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
    M = len(p)
    o = 26 **(M-1) #This is stored to improve the time complexity of the code
    N = len(x)
    l = []
    c = p.index("?")
    r = 26** (M-c-1) #This is stored to improve the time complexity of the code.
    a = horner(p) #The character corresponding to ? is taken as 0 in this case.
    b = horner(x[0:M])
    for i in range(N-M+1):
        #The character present at position i+c in x is irrelevant to the code.
        #So the hash os the character present at index i+c of x is added to a so that it doesn't affect the result.
        if (a + r*hash(x[i+c]))%q == b%q: 
            l.append(i)
        if i < N-M:
            #This new b is the hash function of the next block of text of length M in the string x.
            # It removes the first character and adds the immidiate next character of the substring to generate a new b.
            b = ((26*(b - (o*hash(x[i]))) + (hash(x[i+M])))%q + q)%q
    return l