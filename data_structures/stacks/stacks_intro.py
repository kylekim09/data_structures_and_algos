# can be basically a list/array. you essentially need to ensure you follow the LIFO approach with stacks.
# you can even follow the recursive approach to a stack. 

# Here instead we will go with the iterative approach with a class that is essentially a wrapper around the list class
class Stack():
  __init__ (self):
    self.items = []

  def push (self, item):
    self.items.append(item)

  def pop (self):
    self.items.pop()

  def peek(self);
    return self.items[len(self.items) - 1]

myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())