# to find the maximum element in a list using a linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_max_element(head):
    max_element = float('-inf')
    current = head
    while current:
        max_element = max(max_element, current.data)
        current = current.next
    return max_element


head = Node(1)
node2 = Node(5)
node3 = Node(3)
node4 = Node(8)
node5 = Node(2)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

max_element = find_max_element(head)
print(max_element)  # output 8