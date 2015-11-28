def gen_irrational_string(num):
	string = ""
	i = 1
	while len(string) < num:
		string += str(i)
		i+=1
	return string

irrationalString = "0" + gen_irrational_string(1000001)
product = int(irrationalString[1]) * int(irrationalString[10]) * int(irrationalString[100]) * int(irrationalString[1000]) * int(irrationalString[10000]) * int(irrationalString[100000]) * int(irrationalString[1000000])
print "Product is: " + str(product)