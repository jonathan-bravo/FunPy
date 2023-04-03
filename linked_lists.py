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

    def insertion(self, pos, new):
        self.val.append(new)
        self.num.append(self.num[-1] + 1)
        new_loc = self.num[-1]
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

    def print_forward(self):
        temp = [nu for tu in zip(self.num, self.val) for nu in tu]
        pl = [temp[temp.index(self.prv[self.prv.index(None) + 1]) + 1]]
        [pl.append(temp[temp.index(i) + 1]) for i in self.nxt if i != None]
        print(pl)

    def print_reverse(self):
        temp = [nu for tu in zip(self.num, self.val) for nu in tu]
        pl = [temp[temp.index(self.nxt[self.nxt.index(None) - 1]) + 1]]
        [pl.append(temp[temp.index(i) + 1]) for i in self.prv[::-1] if i != None]
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

def main():
    val = [5, 10, 15]
            
    test = Llist(val)

    test.forwardRead()
    test.reverseRead()

    test.insertion(2,20)
    test.forwardRead()
    test.reverseRead()

    test.delete(2)
    test.forwardRead()
    test.reverseRead()

if __name__ == '__main__':
    main()