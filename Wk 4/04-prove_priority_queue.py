"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""
#Note: I ran out of time, had a bit of a situation with my wife's health, and that's on me.
#Hopefully some semblance of an idea of what this test is supposed to do will count towards
#something.

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(priority, value)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority >= self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

class Fifo:
    def __init__(self):
        self.first = None
        self.last = None
    def append(self, data):
        node = [data, None]  # [payload, 'pointer'] "pair"
        if self.first is None:
            self.first = node
        else:
            self.last[1] = node
        self.last = node
    def pop(self):
        if self.first is None :
            raise IndexError
        node = self.first
        self.first = node[1]
        return node[0]
# Test Cases

# Test
# Scenario: Ideally should append 10 new variables based on what script the user runs, then 20.  We then pop out the most recent appends, then append some more, then pop out two inputs twice.
# Expected Result: 

def main():
    print("Test Case")


if __name__=='__main__':
    #Run a test/example when run as a script:
    a = Fifo()
    a.append(10)
    a.append(20)
    print:a.pop()
    a.append(5)
    print:a.pop()
    print:a.pop()