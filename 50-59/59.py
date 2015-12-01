message = ''

with open('59.txt','r') as f:
	message = f.read()


message = message.split(',')
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
				if newChar in "#$%^&*[]{}|~`+=<>@":
					continue
				decrypted += newChar
				currKey += 1
				if currKey > 2:
					currKey = 0
			word_score = decrypted.count(' ')
			if word_score > highest_word_score:
				highest_word_score = word_score
				print decrypted
				print "Key: \'" + str((unichr(a) + unichr(b) + unichr(c))) + "\' Sum: " +str(sum([ord(i) for i in list(decrypted)]))
