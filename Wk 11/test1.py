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

#Test/Driver
queue = Queue(10)
queue.DeQueue()
queue.DeQueue()
queue.EnQueue()
queue.DeQueue()
queue.DeQueue()
queue.DeQueue()