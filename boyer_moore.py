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

	i = M-1
	for j in range(M-2, -1, -1):
		print(i, j)
		if pattern[j] == pattern[i]:
			i -= 1 # move both i and j to the left
		else:
			delta2[i] = max(delta2[i], j+1) # for the moment store the rightmost re-occurence of the
												# suffix starting from j+1
			i = M - 1 # reset i to the end of suffix

	delta2[i] = max(delta2[i], 0) # for the moment store the rightmost re-occurence

	delta2[-1] = 1

	return delta2


pattern = "ABCXABCC"
print(build_delta2(pattern))






