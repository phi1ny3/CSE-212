"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 1

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online. Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Queue:
    """
    A basic implementation of a Queue
    """

    def __init__(self):
        """
        Start with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.insert(0, value)

    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0
    
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Provide a string representation for this object.
        """
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result


class Taking_Turns_Queue:
    """
    This queue is circular.  When people are added via add_person, then they are added to the 
    back of the queue (per FIFO rules).  When get_next_person is called, the next person
    in the queue is displayed and then they are placed back into the back of the queue.  Thus,
    each person stays in the queue and is given turns.  When a person is added to the queue, 
    a turns parameter is provided to identify how many turns they will be given.  If the turns is 0 or
    less than they will stay in the queue forever.  If a person is out of turns then they will 
    not be added back into the queue.
    """

    class Person:
        """
        A person is defined with a name and a number of turns.
        """

        def __init__(self, name, turns):
            """
            Initialize the person
            """
            self.name = name
            self.turns = turns

        def __str__(self):
            """
            Support the display of single person.
            """
            if self.turns <= 0:
                result = "({}:Forever)".format(self.name)
            else:
                result = "({}:{})".format(self.name, self.turns)
            return result

    def __init__(self):
        """ 
        Start with an empty queue
        """
        self.people = Queue()

    def add_person(self, name, turns):
        """
        Add new people to the queue with a name and number of turns
        """
        person = Taking_Turns_Queue.Person(name, turns)
        self.people.enqueue(person)

    def get_next_person(self):
        """
        Get the next person in the queue and display them.  The person should
        go to the back of the queue again unless the turns variable shows that they 
        have no more turns left.  Note that a turns value of 0 or less means the 
        person has an infinite number of turns.  An error message is displayed 
        if the queue is empty.
        """
        if self.people.is_empty():
            print("No one in the queue.")
        else:
            person = self.people.dequeue()
            if person.turns > 1:  
                person.turns -= 1 
                self.people.enqueue(person)
            print(person.name)

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.people)

    def __str__(self):
        """
        Provide a string representation of everyone in the queue
        """
        return str(self.people)

# Implement Queue using List(Functions)
q=[]
def Enqueue():
    if len(q)==size: # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")
def dequeue():
    if not q:# or if len(stack)==0
        print("Queue is Empty!!!")
    else:
        e=q.pop(0)
        print("element removed!!:",e)
def display():
    print(q)
    
size=int(input("Enter the size of Queue:"))
while True:
    print("Select the Operation:1.Add 2.Delete 3. Display 4. Quit")
    choice=int(input())
    if choice==1:
        Enqueue()
    elif choice==2:
        dequeue()
    elif choice==3: 
        display()
    elif choice==4:
        break
    else:
        print("Invalid Option!!!")


# Test Cases

# Test 1
# Scenario: Create a queue with the following people and turns: Bob (2), Tim (5), Sue (3) and
#           run until the queue is empty
# Exepcted Result: Bob, Tim, Sue, Bob, Tim, Sue, Tim, Sue, Tim, Tim
print("Test 1")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 5)
players.add_person("Sue", 3)
print(players)    # This can be un-commented out for debug help
while len(players) > 0:
    players.get_next_person()
# Defect(s) Found: There is nothing in add_person to prioritize or sort people by # of turns,
# so they're being added consecutively by the same name in that order to the list instead of
# treating each individual instance of name with turn

print("=================")

# Test 2
# Scenario: Create a queue with the following people and turns: Bob (2), Tim (5), Sue (3)
#           After running 5 times, add George with 3 turns.  Run until the queue is empty.
# Exepcted Result: Bob, Tim, Sue, Bob, Tim, Sue, Tim, George, Sue, Tim, George, Tim, George
print("Test 2")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 5)
players.add_person("Sue", 3)
for i in range(5):
    players.get_next_person()
print(players)
players.add_person("George", 3)
print(players)
while len(players) > 0:
    players.get_next_person()
# Defect(s) Found: The iteration is such where it first goes through printing the first names based on popped order
# but it's then taking the remaining 5 for the range of i to put George in

print("=================")

# Test 3
# Scenario: Create a queue with the following people and turns: Bob (2), Tim (Forever), Sue (3)
#           Run 10 times.
# Exepcted Result: Bob, Tim, Sue, Bob, Tim, Sue, Tim, Sue, Tim, Tim
print("Test 3")
players = Taking_Turns_Queue()
players.add_person("Bob", 2)
players.add_person("Tim", 0)
players.add_person("Sue", 3)
print(players)
for i in range(10):
    players.get_next_person()
print(players) 
print(i)   
# Defect(s) Found: There is no way to set a condition for Tim's turns to grow within the limit of 10
# unless we check for whether the list is empty to add more Tim's

print("=================")

# Test 4
# Scenario: Try to get the next person from an empty queue
# Exepcted Result: Error message should be displayed
print("Test 4")
players = Taking_Turns_Queue()
players.get_next_person()
if Taking_Turns_Queue.get_next_person == None:
    quit()
# Defect(s) Found: No errors, it shows as intended, just with a different error message.
    