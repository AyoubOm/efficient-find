from timeit import timeit

def readText(filename):
	text = ""
	with open(filename, 'r') as f:
		for l in f.read().splitlines():
			text += l
	return text


def simple_find(text, word):
	numberOcc = 0
	for i in range(len(text)):
		if text[i:i+len(word)] == word:
			numberOcc += 1

	print(str(numberOcc)+" matches found.")


def rabinKarp(text, word):
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



		
text = readText("sample.txt")
text *= 500
print("size of text: ", len(text))
pattern = "commodo mollis, magna. Vestibulum ullamcorper"



t = timeit('simple_find(text, pattern)', 
	setup="from __main__ import simple_find, readText, text, pattern", number=1)

print("execution time:", t)

# t = timeit('rabinKarp(generate(text, 500), "commodo")', 
# 	setup="from __main__ import rabinKarp, generate, text", number=1)

# print(t)
