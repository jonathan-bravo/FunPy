#!/usr/bin/env python3

from dataclasses import dataclass, field

@dataclass
class Llist:
    val: list = field(default_factory=list)
    num: list = field(default_factory=list)
    nxt: list = field(default_factory=list)
    prv: list = field(default_factory=list)

    def __post_init__(self):
        self.num = list(range(1,len(self.val) + 1))
        self.nxt = [i if i != len(self.val)+1 else None for i in range(2, len(self.val)+2)]
        self.prv = [i if i != 0 else None for i in range(len(self.val))]

    def extend_nxt(self, pos, loc):
        nxt = list()
        [nxt.extend([self.prv[self.prv.index(self.nxt[0])-1],x]) if pos == 1 and i == 0 else nxt.append(x) if i+1 != pos else nxt.extend([loc,x]) for i,x in enumerate(self.nxt)]
        return nxt
    
    def extend_prv(self, loc):
        prv = list()
        if loc in self.nxt:
            [prv.append(x) if self.nxt[self.nxt.index(loc)-1] != self.prv[i] else prv.extend([x,loc]) for i,x in enumerate(self.prv)]
        else:
            [prv.extend([x,loc]) if i == 0 else prv.append(x) for i,x in enumerate(self.prv)]
        return prv
		
    def insertion(self, pos, new):
        self.val.append(new) # add the value to the list
        self.num.append(self.num[-1] + 1) # add next count to end
        self.nxt = self.extend_nxt(pos, self.num[-1])
        self.prv = self.extend_prv(self.num[-1])
		
    def print_forward(self):
        temp = dict()
        [temp.setdefault(n,v) for n,v in zip(self.num, self.val)]
        pl = [temp[self.prv[1]]] # adding first value in forward print
        [pl.append(temp[i]) for i in self.nxt if i != None] # adding all subsequent values
        return pl
		
    def print_reverse(self):
        temp = dict()
        [temp.setdefault(n,v) for n,v in zip(self.num, self.val)]
        pl = [temp[self.nxt[-2]]]
        [pl.append(temp[i]) for i in self.prv[::-1] if i != None]

        return pl
		
    def delete(self, pos):
        pl = self.print_forward()
        del_val = pl[pos]
        del_index = self.val.index(del_val)+1
        self.num.pop(self.num.index(del_index))
        self.nxt.pop(self.nxt.index(del_index))
        self.prv.pop(self.prv.index(del_index))
        self.val.pop(self.val.index(del_val))

def main():
    val = [5, 10, 15]

    test = Llist(val)

    print(test.print_forward())
    print(test.print_reverse())
    print('')

    test.insertion(2,20)
    print(test.print_forward())
    print(test.print_reverse())
    print('')

    test.insertion(1,20)
    print(test.print_forward())
    print(test.print_reverse())
    print('')

    test.delete(2)
    print(test.print_forward())
    print(test.print_reverse())
    print('')

if __name__ == '__main__':
	main()