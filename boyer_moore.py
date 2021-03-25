import string

def find(text, pattern):

	delta1 = build_delta1(pattern)
	delta2 = build_delta2(pattern)


def build_delta1(pattern):
	alphabet = string.ascii_lowercase
	delta1 = {}
	for c in alphabet: delta1[c] = -1
	for i, c in enumerate(pattern): delta1[c] = i
	return delta1


def build_delta2(pattern):
	M = len(pattern)
	delta2 = [-1]*M

	for j in range(M-2, -1, -1):
		i = j-1
		while i >= -1:
			if i == -1 or pattern[i] != pattern[j]: # i == -1 in case of a suffix re-ocurence at the beginning of pattern
				k = i+1
				while k + j - i < M and pattern[k] == pattern[k+j-i]:
					k += 1
				if k + j - i == M:
					delta2[j] = i+1
					break
			i -= 1

	return delta2



pattern = "KBCAB"
print(build_delta2(pattern))






