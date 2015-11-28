message = ''

with open('59.txt','r') as f:
	message = f.read()

contents = ''
with open("59-words.txt","r") as f:
	contents = f.read()

contents = contents.split(",")
parsed_contents = list()
for name in contents:
	parsed_contents.append(name.strip("\""))

message = message.split(',')
words = parsed_contents
highest_word_score = 0
for a in range(ord('a'), ord('z') + 1):
	for b in range(ord('a'), ord('z') + 1):
		for c in range(ord('a'), ord('z') + 1):
			currKey = 0
			decrypted = ""
			for char in message:
				cipher = ''
				if currKey == 0:
					cipher = a
				elif currKey == 1:
					cipher = b
				elif currKey == 2:
					cipher = c
				newChar = str(unichr((int(char) ^ cipher)))
				if newChar in "#$%^&*[]{}|~`":
					continue
				decrypted += newChar
				currKey += 1
				if currKey > 2:
					currKey = 0
			word_score = decrypted.count(' ')
			if word_score > highest_word_score:
				highest_word_score = word_score
				print decrypted
				print sum([ord(i) for i in list(decrypted)])