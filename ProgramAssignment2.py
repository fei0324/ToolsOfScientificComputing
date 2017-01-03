from decimal import *
import math
import random

"""
Programming Assignment One
"""

# Generating Square Root of 2
def generateSqrt2(k):
	xa = 2
	getcontext().prec = 40
	for i in range(0,k):
		xb = Decimal(0.5)*(xa + (2*Decimal(str(xa))**Decimal(-1)))
		xa = xb
	print("Sqrt2 = " + str(xb))

generateSqrt2(6)

"""
a)	Iterations: 4 Approximation: Sqrt2 = 1.4142135623746898698271934335934929 Correct Digits: 12
	Iterations: 5 Approximation: Sqrt2 = 1.4142135623730950488016896235025302 Correct Digits: 23
	Iterations: 6 Aapproximation: Sqrt2 = 1.414213562373095048801688724209698078570 Correct Digits: 38
b)  It took me 4 iterations to get 12 digits and 5 to get 23 and 6 to get 38.
"""

# Generating Square Root of p where p is a prime
def generateSqrtp(p, k):
	xa = p
	getcontext().prec = 20
	for i in range(0,k):
		xb = (1/2)*(xa + (p/xa))
		xa = xb
	print("Sqrt" + str(p) + " = " + str(Decimal(xb)))

generateSqrtp(3, 10)
generateSqrtp(5, 10)
generateSqrtp(7, 10)

"""
c)  Yes, the recursion does generate square root of prime p.
	Using the function generateSqrtp, I was able to get:
	Sqrt3 = 1.732050807568877193176604123436845839023590087890625
	Sqrt5 = 2.236067977499789805051477742381393909454345703125
	Sqrt7 = 2.64575131106459071617109657381661236286163330078125
"""

# Generating Square Root of 2 Using Fraction Expansion
def fractionSqrt2(k):
	y = 2
	getcontext().prec = 35
	for i in range(0, k):
		y = 2 + 1/Decimal(str(y))
	print("Sqrt2 (fraction expansion) = " + str(1+1/y))

fractionSqrt2(37)

"""
d)  Iterations: 4 Approximation: Sqrt2 (fraction expansion) = 1.41428571428571436818799611501162 Correct Digits: 5
	Iterations: 10 Approximations: Sqrt2 (fraction expansion) = 1.414213564213564255922506163187 Correct Digits: 9
	Iterations: 20 Approximations: Sqrt2 (fraction expansion) = 1.4142135623730950894848637061937438 Correct Digits: 16
	Iterations: 25 Approximation: Sqrt2 (fraction expansion) = 1.4142135623730950487956400807542600 Correct Digits: 22
	Iterations: 37 Approximation: Sqrt2 (fraction expansion) = 1.4142135623730950488016887242057622 Correct Digits: 30
"""

# Generating the Golden Ratio
def generatePhi(k):
	fa1 = fa2 = 1
	fb1 = fb2 = 1
	getcontext().prec = 35
	for i in range(0, k):
		fc1 = fb1 + fa1
		fa1 = fb1
		fb1 = fc1
	for j in range(0, k-1):
		fc2 = fb2 + fa2
		fa2 = fb2
		fb2 = fc2
	print("Phi = " + str(Decimal(str(fc1))/Decimal(str(fc2))))

generatePhi(70)

"""
b)  Iterations: 25 Approximation: Phi = 1.6180339887802426268592626001918688 Correct DIgits: 11
	Iterations: 40 Approximation: Phi = 1.6180339887498949025257388711906969 Correct Digits: 16
	Iterations: 50 Approximation: Phi = 1.6180339887498948482035085192411813 Correct Digits: 20
	Iterations: 70 Approximation: Phi = 1.6180339887498948482045868343609257 Correct Digits: 30
c)  It took about 25 iterations to get 11 correct digits, 40 iterations to get 16 correct digits, 50 to get 20 digits and 70 to get 30 digits.
"""

# Computing Phi using Newton-Raphson Method
def newPhi(k):
	xa = 2
	getcontext().prec = 60
	for i in range(0, k):
		xb = xa - (Decimal(str(xa))**2 - xa - 1)/(2*Decimal(str(xa)) - 1)
		xa = xb
	print("newPhi = " + str(xb))

newPhi(6)

"""
d)  Iterations: 4 Approximation: newPhi = 1.618033988749989049438227084465324878692626953125 Correct Digits: 13
	Iterations: 5 Approximation: newPhi = 1.6180339887498949025257388711906969547271728515625 Correct Digits: 16
	Iterations: 6 Approximation: newPhi = 1.61803398874989484820458683436563811772030917980576286919292 Correct Digits: 55
4)  THe Newton-Raphson method works better since it converges much more quickly.
	Iterating 5 times with the Newton-Raphson method already generates 15 digits which is the equivalent of iterating approximately 40 times using fraction expansion.
"""

# Generating Pi using Monte Carlo Method
def generatePi(k):
	inCircle = 0
	outCircle = 0
	getcontext().prec = 20
	for i in range(0, k):
		x1 = random.uniform(0, 1)
		y1 = random.uniform(0, 1)
		if math.sqrt(x1**2 + y1**2) <=1:
			inCircle += 1
		else:
			outCircle += 1
	pi = Decimal(4)*Decimal(str(inCircle))/Decimal(str(inCircle+outCircle))
	print("Pi = " + str(pi))

generatePi(10000)
"""
a)  Iterations: 100 Approximation: Pi = 3.08 Correct Digits: 1
	Iterations: 10,000 Approximation: Pi = 3.1507999999999998231 Correct Digits: 2
	Iterations: 1,000,000 Approximation: Pi = 3.1414599999999999191 Correct Digits: 4
	Iterations: 10,000,000 Approximation: Pi = 3.1415975999999998791 COrrect Digits: 6
	This algorithm is grately affected by the random coordinates that we generated, which cost a lot of inconsistance.
	Iterating 10,000,000 times might only give us 3 digits sometimes and 5 digits some other times.
"""

"""
Programming Assignment Two
"""

# Generating Pi with Continued Fraction Expansion
def serialpi(k):
	# x in this case is everything below 4, which is why for the final answer, we are printing out 4/x
	x = 2*k-1 + k**2
	for i in range(k, 0, -1):
		x = 2*i-1 + i**2/x
	print("FractionPi = " + str(4/x))

serialpi(100)

"""
	Approximation: FractionPi = 3.141592653589793
	All the digits shown for pi are correct. The result we got stops changing after getting here.
"""

# Generating Pi with Precision Decimal
def serialpiprecise(k, precision):
	getcontext().prec = precision
	x = 2*k-1 + k**2
	for i in range(k, 0, -1):
		x = 2*i-1 + i**2/Decimal(str(x))
	print("PiPrecision = " + str(4/x))

serialpiprecise(1000, 10)

"""
This method converges really quickly. With 1000 iterations, the method generates about 800 correct digits.
"""

def eulerpi(n):
	# my eulerpi(2) returns 2.44948974278
	x = 0
	for i in range(1, n):
		# x is pi^2/6
		x = x + 1/i**2
	print("EulerPi = " + str(math.sqrt(6*x)))

eulerpi(1000000)
# Iterating the function for approximately 100,000 times gives us the first 6 correct digits

