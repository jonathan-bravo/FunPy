def f(x):
	return x**3+2*x-3

def newraph(x, t = .001):
	while f(x) > t:
		m = (f(x + t) - f(x - t)) / (2 * t)
		c = (-m * x) + f(x)
		x = (- c) / m
	return print(x)

# this version allows a user to input a function as a string list('function')
def newraph2(x, fx = list('x**3+2*x-3'), t = .001):
	fxt = ['(x+t)' if i=='x' else i for i in fx]
	fx = ''.join(fx)
	fxt = ''.join(fxt)
	while eval(fx) > t:
		m = (eval(fxt) - eval(fx)) / t
		c = (- m * x) + eval(fx)
		x = (- c) / m
	return print(x)