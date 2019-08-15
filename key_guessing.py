from util import *

def guess(pairs, bits, difference, rounds):
	counters = {}
	keys = {}
	count = sum(len(b) for b in bits.values())
	for i in range(2**count):
		counters[i] = 0
		keys[i] = {}
		for p in pairs:
			l1 = p[0] >> WS         #Change to compose
			l2 = p[1] >> WS
			r1 = p[0] % (1 << WS)
			r2 = p[1] % (1 << WS)
			r = rounds - 1
			while r in bits:
				key = 0
				for b in bits[r]:
					key |= ((1 & ((i >> (count//len(bits.keys()) * list(bits.keys()).index(r))) >> b)) << b)
				keys[i][r] = key
				l1, r1 = r1, f(r1) ^ l1 ^ key
				l2, r2 = r2, f(r2) ^ l2 ^ key
				r -= 1
			if ((r1^r2) << WS) + (l1 ^ f(r1) ^ l2 ^ f(r2)) == difference: counters[i] += 1
	rcounters = {v: k for k, v in counters.items()}
	return keys[rcounters[max(rcounters.keys())]]

if __name__ == "__main__":
	print(guess([(0, 0)], {17: (0,), 16: (1,), 15: (0,)}, 0, 18))
