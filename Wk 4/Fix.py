# Taking_Turns_Queue class
class Taking_Turns_Queue:
    # defining an inner class to represent a Person
    class Person:
        # constructor taking name and number of turns
        def __init__(self, name, turns):
            self.name = name
            self.turns = turns
            self.next = None  # reference to next person

    # constructor of the Taking_Turns_Queue class
    def __init__(self):
        # defining a reference to back node of the queue
        self.back = None

    # method to add a person with given name and turns
    def add_person(self, name, turns):
        # creating a Person node
        person = Taking_Turns_Queue.Person(name, turns)
        # if queue is currently empty, adding as back node
        if self.back == None:
            self.back = person
            person.next = person  # and linking p to itself since its a circular queue
        else:
            # otherwise finding front node, which will be the next of back node
            front = self.back.next
            # setting front as next of p
            person.next = front
            # setting p as next of back
            self.back.next = person
            # setting p as new back
            self.back = person

    # removes and displays the person at front
    def get_next_person(self):
        # if queue is empty, displaying error
        if self.back == None:
            print("Queue is empty!")
        else:
            # otherwise fetching front node/person
            node = self.back.next
            # if it is back itself, queue has 1 person, removing it by setting back to None
            if node == self.back:
                self.back = None
            # otherwise setting node.next as next of back
            else:
                self.back.next = node.next
            # printing dequeued person's name
            print('Dequeued:', node.name)
            # if number of turns is 0 or negative, adding back the person, to the back of the queue
            if node.turns <= 0:
                self.add_person(node.name, node.turns)
            # otherwise if turns is greater than 1, adding back with one less turn
            elif node.turns > 1:
                self.add_person(node.name, node.turns - 1)
            # if number of turns was 1, person is not added again

    # this method returns True if queue is empty, else False
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.people)
    def is_empty(self):
        return self.back == None

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