import string


def build_delta1(pattern):
	alphabet = string.ascii_lowercase + string.ascii_uppercase + ' ' + string.punctuation
	delta1 = {}
	for c in alphabet: delta1[c] = -1
	for i, c in enumerate(pattern): delta1[c] = i
	return delta1


def build_delta2(pattern):
	M = len(pattern)
	delta2 = [-1]*(M-1)+[1]

	for j in range(M-2, -1, -1):
		for i in range(M-2, -1, -1):
			if i - (M-1-j) >= 0 and pattern[i - (M-1-j)] == pattern[j]: #checking that the beginning of re-occurence is not = pattern[j]
				continue
			
			k = M-1
			while k > j and i+k-(M-1) >= 0 and pattern[k] == pattern[i+k-(M-1)]:
				k -= 1
			if i+k-(M-1) < 0: # (M-1-k) suffix is matching with the beginning of the pattern
				delta2[j] = k-j+M # (M-1-j) + M - (M-1-k) do like if we will move the pointer all the way to end
								# and substract the matched subsuffix (example ABCXXXABC for j at second X for e.g)
				break
			elif k == j:
				delta2[j] = i-(M-1-j)
				delta2[j] = (j-delta2[j]) + (M-j-1)
				break

		if delta2[j] == -1:
			delta2[j] = (M-j-1) + M # will move j to the end of the pattern + move it along all pattern (whole pattern shifted)

	return delta2



def find(text, pattern):
	N, M = len(text), len(pattern)

	delta1 = build_delta1(pattern)
	delta2 = build_delta2(pattern)
	nbMacthes = 0
	i = M - 1

	while i < N:
		j = M-1
		while j >= 0 and text[i] == pattern[j]:
			j -= 1
			i -= 1

		if j >= 0:
			i += max(M-1-delta1[text[i]], delta2[j])
		else:
			nbMacthes += 1
			i += M + 1

	print("Number of matches:", nbMacthes)







