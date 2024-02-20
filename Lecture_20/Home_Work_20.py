"""1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList  კლასი რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.
   2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
   3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
 """

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node



    def remove(self):
        if self.head is None:
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None


    def print_linked_list(self):
        current_node = self.head

        while(current_node):
            if current_node.next:
                print(f"{current_node.value}", end=' -> ')
            else:
                print(f"{current_node.value}")
            current_node = current_node.next


# #======================================
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Linked_List is: ", end= "")
linked_list.print_linked_list()

linked_list.remove()
print("After last item removed Linked_List is: ", end= "")
linked_list.print_linked_list()

linked_list.remove()
print("After last item removed Linked_List is: ", end= "")
linked_list.print_linked_list()

"""
4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def __str__(self):  # Changed print to __str__
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(f"New stack is: {stack}")

stack.pop()
stack.pop()
print(f"Popped stack is: {stack}")
        
