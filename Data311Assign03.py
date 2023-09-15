class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
 
class linkedList: # creating list
    def __init__(self, head=None):
        self.head = head 

    def getCount(self): #defining getCount function
            temp = self.head
            count = 0
     
            while (temp):
                count += 1
                temp = temp.next
            return count

    def push(self, new_data): #defining push function
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode
 
    def locate(self, x): #defining locate function
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False
    
  
    def __str__(self):    
          r = ""
          while self.head:
              r += "[" + str(self.head.data) + "]" + ", "  # formating the SLL in the way desired
              self.head = self.head.next
          r = r.strip(", ")
          if len(r):
              return "(" + r + ")"
          else:
              return "[]"

    
    def printSLL(self): #defining print function
      if llist.getCount() == 0:
        print("Empty Linked List")
      else:
        print(llist)
        

#Empty Linked list call
if __name__ == '__main__':
    print("Empty Linked list call")
    llist = linkedList()

 
    if llist.locate(5):
        print("Is the item '5' located? Yes")
    else:
        print("Is the item '5' located? No")
    
    llist.printSLL()
    print("\n")

#Singular Linked list call    
if __name__ == '__main__':
    print("Singular Linked list call")
    llist = linkedList()
    llist.push(1)


    if llist.locate(2):
        print("Is the item '5' located? Yes")
    else:
        print("Is the item '5' located? No")
    
    llist.printSLL()
    print("\n")
    
#Multiple Linked list call    
if __name__ == '__main__':
    print("Multiple Linked list call")
    llist = linkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)

 
    if llist.locate(2):
        print("Is the item '5' located? Yes")
    else:
        print("Is the item '5' located? No")
    
    llist.printSLL()
    print("\n")

#Part 2

class Stack: #creating stack
  def __init__(self):
    self.items = []

  def isEmpty(self): 
    return self.items == []

  def push(self, item): #defining push function
    self.items.append(item)

  def pop(self): #defining pop function
    if self.items:
      return self.items.pop()
    else:
      return print("Error")


  def peek(self): #defining peek function
    return self.items[len(self.items)-1]

  def size(self): #defining size function
    return len(self.items)

def calculate(operator, operand1, operand2): #defining function to do the math
    if operator =="*":
        return operand1 * operand2
    elif operator =="/":
        return operand1 / operand2
    elif operator =="+":
        return operand1 + operand2
    else:
        return operand1 - operand2

def evaluate(e): #defining evaluate function
    operandStack = Stack()
    tokenList = list(e)
    if len(tokenList) == 0 or tokenList[0] == " ":
      print("Error: []") # Printing error upon conditon
      return
    if tokenList[0] not in "0123456789":
      print("Error: Operand before integer " + tokenList[0]) # Printing error upon conditon
      return
    
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            operator = token
            result = calculate(operator, operand1, operand2)
            operandStack.push(result)
    return(operandStack.pop())

 #Testing 
print("Solving the Post Fix Evaluation of '1'")
print("Answer: ", evaluate("1"))
print("\n")
print("Solving the Post Fix Evaluation of '+'")
print("Answer: ", evaluate("+"))
print("\n")
print("Solving the Post Fix Evaluation of '1 2 3 4'")
print("Answer: ", evaluate("1234"))
print("\n")
print("Solving the Post Fix Evaluation of '1 2 +'")
print("Answer: ", evaluate("12+"))
print("\n")
print("Solving the Post Fix Evaluation of '2 5 - 3 / 2 *'")
print("Answer: ", evaluate("25-3/2*"))
print("\n")
print("Solving the Post Fix Evaluation of '1 -'")
print("Answer: ", evaluate("1-"))
print("\n")
