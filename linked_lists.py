class Llist:
	def __init__(self, num, nxt, prv, val):
		self.num, self.nxt, self.prv, self.val = num, nxt, prv, val
	def insertion(self, pos, new):
		self.val.append(new)
		self.num.append(self.num[-1] + 1)
		new_loc = num[-1]
		new_nxt = []
		new_prv = []
		n = 0
		p = 0
		while n != len(self.nxt):
			if n+1 == pos:
				new_nxt.append(new_loc)	
			new_nxt.append(self.nxt[n])
			n += 1
		self.nxt = new_nxt
		while p != len(self.prv):
			new_prv.append(self.prv[p])
			if self.nxt[self.nxt.index(new_loc)-1] == self.prv[p]:
				new_prv.append(new_loc)
			p += 1
		self.prv = new_prv
	def forwardRead(self):
		temp = []
		pl = []
		for i,v in zip(self.num, self.val):
			temp.append(i)
			temp.append(v)
		pl.append(temp[temp.index(self.prv[self.prv.index(None) + 1]) + 1])
		for i in self.nxt:
			if i == None:
				break
			pl.append(temp[temp.index(i) + 1])	
		print(pl)	
	def reverseRead(self):
		temp = []
		pl = []
		for i,v in zip(self.num, self.val):
			temp.append(i)
			temp.append(v)
		pl.append(temp[temp.index(self.nxt[self.nxt.index(None) - 1]) + 1])
		for i in self.prv[::-1]:
			if i == None:
				break
			pl.append(temp[temp.index(i) + 1])	
		print(pl)
	def delete(self, pos):
		temp = []
		pl = []
		for i,v in zip(self.num, self.val):
			temp.append(i)
			temp.append(v)
		pl.append(temp[temp.index(self.nxt[self.nxt.index(None) - 1]) + 1])
		for i in self.nxt:
			if i == None:
				break
			pl.append(temp[temp.index(i) + 1])
		gone = pl[pos]
		del self.num[self.num.index(temp[temp.index(gone) - 1])]
		del self.nxt[self.nxt.index(temp[temp.index(gone) - 1])]
		del self.prv[self.prv.index(temp[temp.index(gone) - 1])]
		del self.val[self.val.index(temp[temp.index(gone)])]

num = [1, 2, 3]
nxt = [2, 3, None]
prv = [None, 1, 2]
val = [5, 10, 15]
		
test = Llist(num,nxt,prv,val)

test.forwardRead()
test.reverseRead()

test.insertion(2,20)
test.forwardRead()
test.reverseRead()

test.delete(2)
test.forwardRead()
test.reverseRead()