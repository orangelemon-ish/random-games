#asks for a word and checks that it is a) there and b) non-numerical
word = input("Enter a word:")

first = word[0]
root = word[1:]
pyg = "ay"

def pyg_l(n):
	if len(n) > 0 and n.isalpha():
		print ("Normal English: " + n)
		print ("Pyg Latin: " + root + first + pyg)

	else:
		print ("Please try again. Make sure your word only consists of letters.")
		word2 = input("Enter a word:")
		first2 = word2[0]
		root2 = word2[1:]
		if len(word2) > 0 and word2.isalpha():
			print ("Normal English: " + word2)
			print ("Pyg Latin: " + root2 + first2 + pyg)

pyg_l(word)
