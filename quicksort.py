#10 quicksort
def sort(l):
	quicksort(l, 0, len(l) - 1)
	return l

def quicksort(l, b, t):
	if b < t:
		pivot = partition(l, b, t)
		quicksort(l, b, pivot - 1)
		quicksort(l, pivot + 1, t)

def partition(l, b, t):
	pivot = l[t]
	n = b
	for i in range(b, t):
		if l[i] < pivot:
			l[i], l[n] = l[n], l[i]
			n = n + 1
	l[n], l[t] = l[t], l[n]		
	return n

x = [8,6,7,5,3,0,9]

sort(x)