class Basketball_Player:
    
    def __init__(self, name, score):

        self.name = name

        self.score= score

    def _str_(self):

        return "%-16s: %d" % (self.name, self.score)

    def _cmp_(self, other):

        if self.score > other.score: return  1

        if self.score < other.score: return -1

        return 0

#you passed (score,name) but in the definition of class it is (name,score)
Kawhi   = Basketball_Player("Kawhi Leonard",24)

Damian  = Basketball_Player("Damian Lillard",28)

Ethan   = Basketball_Player("Ethan Thompson",15)

class PriorityQueue:
    #to use items list we have to declare it here
    items=[]
    def _init_(self):

        self.items = []

    def is_empty(self):

        return self.items == []

    def insert(self, item):

        self.items.append(item)

    def remove(self):

        maxi = 0

        for i in range(0, len(self.items)):
            
            #you were comparing players instead we have to compare their scores
            if self.items[i].score > self.items[maxi].score:
                maxi = i
        item = self.items[maxi]

        #remove function to remove the item from list
        self.items.remove(item)

        return item

q = PriorityQueue()

q.insert(Kawhi)

q.insert(Damian)

q.insert(Ethan)

while not q.is_empty():
    #you were using remove() twice for the same player instead we must use a single variable
    player=q.remove()
    print(player.name, player.score)