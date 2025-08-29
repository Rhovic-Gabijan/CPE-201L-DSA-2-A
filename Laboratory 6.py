class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def get_head(self):
        return self.head.data if self.head else None
    
    def get_tail(self):
        current = self.head
        if not current:
            return None
        while current.next:
            current = current.next
        return current.data
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            return False
    return True
                
if __name__ == "__main__":
    llist = LinkedList()
    
    for num in range(20):
        if is_prime(num):
            llist.append(num)
            
    print("Prime numbers less than 20 in the linked list:")
    llist.display()
    
    print("Head of the list:", llist.get_head())
    print("Tail of the list:", llist.get_tail())