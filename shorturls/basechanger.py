CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(CHARS)

def decimal2base_n(n):
	if n >= BASE:
		return decimal2base_n(n // BASE) + CHARS[n % BASE]
	else:
		return CHARS[n]

def base_n2decimal(n):
	if len(n) > 1:
		return base_n2decimal(n[:-1]) * BASE + CHARS.index(n[-1])
	else:
		return CHARS.index(n[0])