# work on lifo
#push_add from top
#pop-remove from top

class stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
         return self.items==[]

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


'''s=stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
s.pop()
print("after popping top element",s.get_stack())
'''
s=stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())
s.pop()
s.pop()
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())

