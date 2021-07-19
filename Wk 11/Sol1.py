class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item


class Basketball Player:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)

    def __cmp__(self, other):
        if self.score < other.score: return  1   # less is more
        if self.score > other.score: return -1
        return 0

Kawhi = Basketball Player("Kawhi Leonard", 24.8)
Damian  = Basketball Player("Damian Lillard", 28.8)
Ethan   = Basketball Player("Ethan Thompson", 15.7)
   
q = Queue()
q.insert(Kawhi)
q.insert(Damian)
q.insert(Ethan)
while not q.is_empty(): 
    print(q.remove())
