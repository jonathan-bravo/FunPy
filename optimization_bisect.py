def tester(x):
	return(x**3 + (2 * x) - 3)

# recursively
def bisect(low, high):
	center = (high + low) / 2
	if tester(center) < .001 and tester(center) > -.001:
		return center
	else:	
		if tester(low) < 0 and tester(center) > 0:
			bisect(low, center)
		elif tester(center) < 0 and tester(high) > 0:
			bisect(center, high)

# while loop
