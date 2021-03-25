def find(text, word):
	k = len(word)
	d = 26
	q = 1 << 63 - 1
	p = pow(26, k-1, q)
	
	occ = 0
	hashWord = 0
	for i in range(k):
		hashWord = (hashWord*d + ord(word[i])) % q

	currHash = 0
	for i in range(k):
		currHash = (currHash*d + ord(text[i])) % q

	for i in range(len(text)-k-1):
		if currHash == hashWord:
			if word == text[i:i+k]:
				occ += 1

		currHash -= p*ord(text[i])
		if i + k < len(text):
			currHash = ((currHash*d)%q + ord(text[i+k])) % q

	print("number of occurences:", occ)
