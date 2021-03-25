def simple_find(text, word):
	numberOcc = 0
	for i in range(len(text)):
		if text[i:i+len(word)] == word:
			numberOcc += 1

	print(str(numberOcc)+" matches found.")