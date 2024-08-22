class Node:

    def __init__(self, element):
        self.element = element
        self.next = None

class LinkedList:

    def __init__(self):
        self.head: Node = None
        self.last: Node = None
    
    #
    # Add an element to final index of list.
    #
    def add(self, element):
        node = Node(element)

        #
        # Check if the list is empty.
        #
        if self.is_empty():
            self.head = node
            self.last = node
            return
        
        self.last.next = node
        self.last = node

    def remove(self, element):
        if self.is_empty():  # Check if the list is empty.
            return None

        current = self.head
        previous = None     # Saving node previous to the node to be removed.

        while current is not None:
            if current.element == element:
                if previous is None: 
                    self.head = current.next
                    if self.head is None:  
                        self.last = None
                else:  
                    previous.next = current.next   # Updating the next so that the previous node to be removed is equal to the next of the node that will be removed.
                    if current.next is None:  
                        self.last = previous

                return element

            previous = current
            current = current.next

        return None

    #
    # Check if the linked list is empty.
    #
    def is_empty(self) -> bool:
        return self.head is None
    
    #
    # Return an array with all elements.
    #
    def get_all(self):
        elements = []

        if self.is_empty():
            return elements

        node = self.head
        while True:
            elements.append(node.element)
            node = node.next

            if node is None:
                break
        
        return elements

    #
    # Get the first occurrence of element on list.
    #
    def get(self, element):

        if self.is_empty():
            return None
        
        node = self.head
        while True:

            if node.element == element:
                return node.element
            
            node = node.next
            if node is None:
                break
        
        return None