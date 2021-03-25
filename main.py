from timeit import timeit

def readText(filename):
	text = ""
	with open(filename, 'r') as f:
		for l in f.read().splitlines():
			text += l
	return text


		
text = readText("sample.txt") * 500
pattern = "commodo mollis, magna. Vestibulum ullamcorper"

print("size of text: ", len(text))
print("=====execution time=====")


t = timeit('simple_find(text, pattern)', 
	setup="from simpleFind import simple_find; from __main__ import readText, text, pattern", number=1)

print("simple find:", t)

t = timeit('find(text, pattern)', 
	setup="from __main__ import text, pattern; from boyerMoore import find, build_delta2, build_delta1", number=1)
print("Boyer-Moore:", t)

