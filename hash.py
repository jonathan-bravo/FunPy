class hash_table:
	def __init__(self, values, keys, length):
		values *= (length * 62)
		self.values, self.keys, self.length = values, keys, length
	def convert(self, x):
		b64 = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,'0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61}
		char = list(x)
		temp = 0
		for i in range(len(char)):
			temp += b64[char[i]]
		return temp		
	def hash_func(self, x):
		if len(x) > self.length:
			return 'User names must be ' + str(self.length) + 'charcters/ integers or less' 
		if x in self.keys:
			char = list(x)
			password = self.values[self.convert(x)][self.values[self.convert(x)].index(x)+1]
			check = input('Enter Password: ')
			if check == password:
				return print('Correct password: ' + str(password))
			else:
				return 'Incorrect password'
		else:
			print('User name does not exist. \nMake new user?\n')
			yn = input('yes/no: ')
			if yn == 'yes' or yn == 'y' or yn == 'Y':
				self.keys.append(x)
				char = list(x)
				password = input('Enter a new password: ')
				if len(self.values[self.convert(x)]) == 0:
					self.values[self.convert(x)] = [x, password]
					return print('New user successfully created with password: ' + str(password))
				else:
					self.values[self.convert(x)].append(x)
					self.values[self.convert(x)].append(password)
					return print('New user successfully created with password: ' + str(password))

def make_hash(name, length):
	name = str(name)
	hash_func(values = [[]], keys = [], length = length)

Google = hash_table(values = [[]], keys = [], length = 12)

Google.hash_func('aaa') # example username input

Google.hash_func('PqV') # example username that would create a collision... but doesn't!

Google.hash_func('HaKmonkey') # just for giggles

Google.hash_func('willpearse') # yup