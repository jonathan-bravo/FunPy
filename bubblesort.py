#10 bubblesort
def bubblesort(x, sort = []):
	if len(x) >= 2:
		for i in range(len(x) - 1):
			if x[i] > x[i + 1]:
				x[i], x[i + 1] = x[i + 1], x[i]
		sort.append(x[-1])	
		return bubblesort(x[:len(x) - 1])
	else:
		sort.append(x[-1])
		return sort[::-1]

x = [8,6,7,5,3,3,9]
bubblesort(x)