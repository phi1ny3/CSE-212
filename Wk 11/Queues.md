# Queues
---
## I.  Introduction
So what are queues anyways?  Queues are what are considered "First in, first out", meaning the process of removing an object from the queue will remove it in the order it was queued in to begin with.  Think like a conveyor belt.

Queues are used when we need to process a collection of requests in an orderly way.

## II. Push/Pop or Enqueue/Dequeue
You may be familiar with these terms.  However, the commands for queues differ, and are called enqueue() (for adding), and dequeue() (for removing).  Dequeue can actually "pop" as well, as long as you are taking from the index 0.

|   Order   |      Enqueue/Dequeue position      |
| :-----:   | :------------:                     |
| 1         |1             |1                    |
| 2         |2             |2                    |
| 3         |3             |3                    |
| 4         |4             |4                    |

## III. Functions/Operations on Queues
As mentioned, enqueue and dequeue are the most common operations to use on a queue.  However, there are others.  Size() can ascertain the size of a queue, and empty() can determine if the queue is empty.

Additionally, there are more advanced forms of container classes resembling queues. There are deques, which work off of both sides, and have functions like extendleft(), extend, popleft(), pop(), etc.  Conceptually, adding or removing the element on the left of a deque is behavior associated with a queue.

All of these basic operations/algorithms within the queue have time complexities that are straightforward.  Assuming worst case, the complexity is:
| Operation     | Performance   |
| :-----:       | :------------:|
| enqueue(value)| O(1) |
| dequeue()     | O(n) |
| size()        | O(1) |
| empty()       | O(1) |


## IV. Queues in Flowcharts/Program Planning
Consider an IT service queue, in the simplest terms.  When a customer enters the system, it looks something like this:


![Queues Example](QueuesFlowchart.jpg)




Here, we see how customers go in line first, and leave the queue out first as well.

## V. Example
Considering the queue above, the implementation of the queue in Python would look something like this:
```Python
customer_Queue = queue()
#Time to Enqueue
cust_num = int(input("How many customers are in the system?"))
for i in range(2, cust_num+1):
    customer_Queue.append(i)
    i= i+1


serviced = False
serviced = bool(input("Was the customer served?"))

if serviced == ("True"):
    #Dequeuing in action
    for i in range(2, 0)
        del customer_Queue(i)
        i = i-1
return
```

## VI. Testing Example
1. Here is a good example of a simple Queue program put together:

```Python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):

        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):

        return len(self.queue) == 0
    
    def __len__(self):

        return len(self.queue)

    def __str__(self):
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result
```

## VII Priority Queue
You may have seen the concept of a queue, and wondered "is there a way to organize it by a particular order instead of the order served/put in?" A priority queue works similarly to a queue, except it does the following:
1. An element assigned with a higher priority will be entered in the queue first, even if it further down in service
2. If elements have equal priority, it defaults to queue behavior and orders by the one that came sooner.

The time complexity for this is O(n log n) for insertion usually, and O(1) for pulling.  There are more efficient forms, but we'll use this one to start.

## VIII Advanced Problem

1. Create a Queue class.  It could look something like this to start:
```Python
class PriorityQueue:
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
            #comparing scores
            if self.items[i].score > self.items[maxi].score:
                maxi = i
        item = self.items[maxi]
        #remove function to remove the item from list
        self.items.remove(item)
        return item
```

Create a queue of a class "Basketball Player", that keeps track of names and scores.  It could look like this to begin with (you'll want to add more like in the PriorityQueue Class):
```Python
class Basketball Player:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "%-16s: %d" % (self.name, self.score)
```
How would the queue look like if you were to add Kawhi Leonard, Damian Lillard, and Ethan Thompson?  How would you manipulate a queue to prioritize position in queue by score?

Here is the [Solution](Sol1.py)

[Back to Home](Python_Structures_Tutorial.md)
