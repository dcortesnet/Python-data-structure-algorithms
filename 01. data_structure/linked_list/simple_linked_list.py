class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        

linked_list = LinkedList()
linked_list.append("Data 1")
linked_list.append("Data 2")
linked_list.append("Data 3")

linked_list.display()
        
        