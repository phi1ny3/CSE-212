"""
CSE212 
(c) BYU-Idaho
07-Prove - Problems

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class LinkedList:
    """
    Implement the LinkedList data structure.  The Node class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Node object, we will need to 
    specify LinkedList.Node
    """

    class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    ###################
    # Start Problem 1 #
    ###################
    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        new_node = LinkedList.Node(value) # create a new Node
        if self.head is None: # check is head is None //if True
            self.head = new_node # assign new_node to head
        else: # if false
            curr = self.head # set current to head
            while curr.next is not None: # iterate until current.next is not None
                curr = curr.next # set current to current.next
            # after reaching in last node
            curr.next = new_node  # set current.next to new_node

    #################
    # End Problem 1 #
    #################

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    ###################
    # Start Problem 2 #
    ###################
    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        # check is head is None i.e list is empty
        if self.head is None: # if true
            return # exit from function
        # check is head.next is None i.e list has only 1 element
        elif self.head.next is None: # if true
            self.head = None # set self.head to None
            return # exit from function
        else: # if false
            # create current and set to self.head
            curr = self.head
            # iterate until curr.next.next is not None
            while curr.next.next is not None:
                curr = curr.next # set curr to curr.next
            # after reaching at 2nd last node
            curr.next = None # set curr.next to None

    #################
    # End Problem 2 #
    #################

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    # Connect new node to the node containing 'value'
                    new_node.prev = curr
                    # Connect new node to the node after 'value'
                    new_node.next = curr.next
                    # Connect node after 'value' to the new node
                    curr.next.prev = new_node
                    # Connect the node containing 'value' to the new node
                    curr.next = new_node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    # ###################
    # # Start Problem 3 #
    # ###################
    def remove(self, value):
        """
        Remove the first node that contains 'value'.
    #     """
        #initialize our head and node status variable
        current = self.head
        node_deleted = False
        #if statement for searching along the pointer
        if current is None:
            node_deleted = False
        #If the current value data matches value, remove and move along
        elif current.data == value:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.head.data == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == value:
                    current.prev.next = current.next
                    node_deleted = True
                current = current.next

    # #################
    # # End Problem 3 #
    # #################

    ###################
    # Start Problem 4 #
    ###################
    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        curr = self.head  #Start at the begining since this is a forward iteration.
        while curr is not None: #Loop to iterate through the linked list
            if(curr.data==old_value): #Checks for the values of they match to the old value
                curr.data=new_value #Then they are replaced with the new value
            curr=curr.next

    def display(self):
        curr = self.head
        print("current list : ")
        while curr is not None:
            print (curr.data)
            curr = curr.next

    #################
    # End Problem 4 #
    #################

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    ###################
    # Start Problem 5 #
    ###################
    def __iter__(self):
        temp = self.head
        while(temp!=None):
            yield temp.data
            temp = temp.next

    def __reversed__(self):
        """

        Iterate backward through the Linked List

        """
        temp = self.tail

        while(temp!=None):
            yield temp.data
            temp = temp.prev


    #################
    # End Problem 5 #
    #################

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

    
# Sample Test Cases (may not be comprehensive) 
print("\n=========== PROBLEM 1 TESTS ===========")
ll = LinkedList()
ll.insert_tail(1)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.insert_head(5)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]
ll.insert_tail(0)
ll.insert_tail(-1)
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0, -1]

print("\n=========== PROBLEM 2 TESTS ===========")
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1, 0]
ll.remove_tail()
print(ll) # linkedlist[5, 4, 3, 2, 2, 2, 1]

print("\n=========== PROBLEM 3 TESTS ===========")
ll.insert_after(3, 3.5)
ll.insert_after(5, 6)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(-1)
print(ll) # linkedlist[5, 6, 4, 3, 3.5, 2, 2, 2, 1]
ll.remove(3)
print(ll) # linkedlist[5, 6, 4, 3.5, 2, 2, 2, 1]
ll.remove(6)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2, 1]
ll.remove(1)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(7)
print(ll) # linkedlist[5, 4, 3.5, 2, 2, 2]
ll.remove(5)
print(ll) # linkedlist[4, 3.5, 2, 2, 2]
ll.remove(2)
print(ll) # linkedlist[4, 3.5, 2, 2]

print("\n=========== PROBLEM 4 TESTS ===========")
ll.replace(2, 10)
ll.display()
#print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(7, 5)
ll.display()
#print(ll) # linkedlist[4, 3.5, 10, 10]
ll.replace(4, 100)
ll.display()
#print(ll) # linkedlist[100, 3.5, 10, 10]


print("\n=========== PROBLEM 5 TESTS ===========")
ll = [100,3.5,10,10]
print(list(reversed(ll)))  # [10, 10, 3.5, 100]
#Problem 5 - Reversed Iterator

#The __iter__ function provides the ability to iterate forward through a LinkedList object using a for loop such as for item in my_linkedlist. When a for loop starts, the __iter__ function will start. Each time the yield statement runs, it will provide a new value to the for loop and pause the __iter__ function. When the for loop goes to the next iteration, it will continue running the __iter__ function again until it gets to the next yield which will provide the next value to the for loop. You can use the following test code to see how the __iter__ function works:
#ceate a linked list from the list ll
my_linkedlist = LinkedList()
for x in ll:
    my_linkedlist.insert_head(x)

print("The contents of this linked list are :")
for item in my_linkedlist:
    print(item)

#The __reversed__ function is used to iterate backwards. Implement the __reversed__ function in the LinkedList class. Hint: Pattern your solution after the __iter__ function that was already written for you and that was described above. To test the __reversed__ function, you can use the following code:
print("the contents of the reversed linked list are : ")
for item in reversed(my_linkedlist):
    print(item)