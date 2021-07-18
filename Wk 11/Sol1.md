```Python
class Golfer:
    ...
    def __cmp__(self, other):
        if self.score < other.score: return  1   # less is more
        if self.score > other.score: return -1
        return 0

    tiger = Golfer("Tiger Woods",    61)
    phil  = Golfer("Phil Mickelson", 72)
    hal   = Golfer("Hal Sutton",     69)
   
    pq = PriorityQueue()
    pq.insert(tiger)
    pq.insert(phil)
    pq.insert(hal)
    while not pq.is_empty(): print pq.remove()
        Tiger Woods    : 61
        Hal Sutton     : 69
        Phil Mickelson : 72
```