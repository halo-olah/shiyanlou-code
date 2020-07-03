for x in xrange(1,100):
	if (x%7==0) or ("7" in str(x)):
		continue
	else:
		print(x)