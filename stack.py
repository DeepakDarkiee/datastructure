class Stack:
     def __init__(self):
         self.stack = []

     def add(self,dataval):
         if dataval not in self.stack:
             self.stack.append(dataval)
             return True
         else:
             return False

#      def peek(self):
#          return self.stack[-1]
#
# AStack = Stack()
# AStack.add("mon")
# AStack.add("tue")
# AStack.peek()
# print(AStack.peek())
# AStack.add("wed")
# AStack.add("thu")
# print(AStack.peek())
     def remove(self):
         if len(self.stack)<=0:
             return ("NO Elemnt in Stack")
         else:
             return self.stack.pop()

AStack= Stack()
AStack.add("mon")
AStack.add("tue")
AStack.add("wed")
AStack.add("thu")

print(AStack.remove())
print(AStack.remove())
print(AStack.remove())
print(AStack.remove())
print(AStack.remove())