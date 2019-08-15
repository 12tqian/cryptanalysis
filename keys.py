from util import * 

def reverse(z, r, k1, k2, k3=None, k4=None):
	zi = ((z >> ((61 - r) % 62)) & 1)
	c = 2**WS - 4
	key = zi ^ c ^ (lambda x: rotr(x, 1) ^ x)(rotr(k3 if k4 else k2 if k3 else k1 if k2 else None, 3) ^ (k1 if k4 else 0)) ^ (k4 if k4 else k3 if k3 else k2)
	return key

def crack(z, r, k1, k2, k3, k4):
	keys = [k4, k3, k2, k1]
	r -= 4 if k4 else 3 if k3 else 2 if k2 else None
	while r > 0:
		r -= 1
		k = reverse(z, r, k1, k2, k3, k4)
		k1, k2, k3, k4 = k, k1, k2, k3
		keys.append(k)
	return list(reversed(keys))

if __name__ == "__main__":
	print(crack(0b11111010001001010110000111001101111101000100101011000011100110, 32, k1=54067, k2=52734, k3=50331, k4=34734))
