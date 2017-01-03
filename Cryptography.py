import math

def RSA_encrypt(p, q, e, m):
	# p and q are the two big primes that we picked
	# n = p*q which is the modulus in a RSA public key
	# e is the exponent i.e. gcd(e, (p-1)(q-1)) = 1
	# m is the message we are going to encrypt (a list of integers), plaintext
	n = p*q
	phi = (p-1)*(q-1)
	print("phi = " + str(phi))
	c = [] # c is the ciphertext

	# Check if e is suitable for the chosen p and q
	if gcd(phi, e) != 1:
		print("e = " + str(e))
		print(gcd(phi, e))
		print("e is not suitable for the pair of primes.")
	else:
		d = inverse(e, phi)
		print("d = " + str(d))
		# produce cipher text
		for element in m:
			cipher = divmod(element**e, n)[1]
			c.append(cipher)
		print("Cipher text = " + str(c))
		print("Public key = " + "(" + str(n) + ", " + str(e) + ")")
		print("Private key = " + "(" + str(n) + ", " + str(d) + ")")

def RSA_decrypt(p, q, e, c):
	# c is the cipher text
	n = p*q
	phi = (p-1)*(q-1)
	p = [] #plaintext
	d = inverse(e, phi)
	# produce plain text
	for element in c:
		plaintext = divmod(element**d, n)[1]
		p.append(plaintext)
	print("Plain text = " + str(p))

def CaesarCipher_encrypt(n, m):
	# n is the number of spaces we are shifting
	# m is the plain text in the form of a list of integers
	c = []
	# c is the cipher text in the form of a list of integers
	for element in m:
		cipher = element + n
		if cipher >= 26:
			cipher = cipher - 26
		c.append(cipher)
	print("Cipher text = " + str(c))

def CaesarCipher_decrypt(n, c):
	# n is the number of spaces we are shifting
	# c is the cipher text in the form of a list of integers
	m = []
	# m is the original message (plain text)
	for element in c:
		plain = element - n
		if plain < 0:
			plain = plain + 26
		m.append(plain)
	print("Plain text = " + str(m))

CaesarCipher_encrypt(3, [7, 4, 11, 11, 14, 22, 14, 17, 11, 3])
CaesarCipher_decrypt(3, [10, 7, 14, 14, 17, 25, 17, 20, 14, 6])


# Euclidean algorithm find gcd
def gcd(a, b):
	# input a > b
	r = a%b
	if r == 0:
		return b
	else:
		while r != 0:
			q = math.floor(a/b)
			r = a - b*q
			a = b
			b = r
		# Need to print out n instead of m, since n is now at the position of m after the while loop
		return a

def inverse(u, v):
    # Return the inverse of u mod v.
    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q=divmod(u3, v3)[0]
        u1, v1 = v1, u1 - v1*q
        u3, v3 = v3, u3 - v3*q
    while u1<0:
        u1 = u1 + v
    return u1

RSA_encrypt(173, 149, 3, [7, 14, 22, 0, 17, 4, 24, 14, 20])
RSA_decrypt(173, 149, 3, [343, 2744, 10648, 0, 4913, 64, 13824, 2744, 8000])