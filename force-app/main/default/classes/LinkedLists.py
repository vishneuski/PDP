from collections import deque
# #collections.deque
# # 1 ********************* Define deque - Linked List
# print(deque(['a','b','c']))
# print(deque('abc'))
# print(([{'data': 'a'}, {'data': 'b'}]))

# # 2 *********************  Implement Queue (FIFO) using deque()
# queue = deque()
# #add to queue
# queue.append("Mary")
# queue.append("John")
# queue.append("Susan")
# print(queue)
# #remove from queue
# queue.popleft()
# queue.popleft()
# print(queue)

# # 3 *********************  Implement Stack (LIFO) using deque()
# stack = deque()
# # #add to stack
# stack.appendleft("Mary")
# stack.appendleft("John")
# stack.appendleft("Susan")
# print(stack)
# # #remove from stack
# stack.popleft()
# stack.popleft()
# print(stack)

# # 4 *********************  Create a Linked List
# 4-1 create a class to represent your linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)



# # 5 ********************* 
# # 6 ********************* 
# # 7 ********************* 
# # 8 ********************* 
# # 9 ********************* 
# # 10 ********************* 
# # 11 ********************* 
# # 12 ********************* 






















# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return self.data


# class LinkedList:
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next

#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)

#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next

#     def add_first(self, node):
#         node.next = self.head
#         self.head = node

#     def add_last(self, node):
#         if not self.head:
#             self.head = node
#             return
#         for current_node in self:
#             pass
#         current_node.next = node

#     def add_after(self, target_node_data, new_node):
#         if self.head is None:
#             raise Exception("List is empty")

#         for node in self:
#             if node.data == target_node_data:
#                 new_node.next = node.next
#                 node.next = new_node
#                 return

#         raise Exception("Node with data '%s' not found" % target_node_data)

#     def add_before(self, target_node_data, new_node):
#         if self.head is None:
#             raise Exception("List is empty")

#         if self.head.data == target_node_data:
#             return self.add_first(new_node)

#         prev_node = self.head
#         for node in self:
#             if node.data == target_node_data:
#                 prev_node.next = new_node
#                 new_node.next = node
#                 return
#             prev_node = node

#         raise Exception("Node with data '%s' not found" % target_node_data)

#     def remove_node(self, target_node_data):
#         if self.head is None:
#             raise Exception("List is empty")

#         if self.head.data == target_node_data:
#             self.head = self.head.next
#             return

#         previous_node = self.head
#         for node in self:
#             if node.data == target_node_data:
#                 previous_node.next = node.next
#                 return
#             previous_node = node

#         raise Exception("Node with data '%s' not found" % target_node_data)