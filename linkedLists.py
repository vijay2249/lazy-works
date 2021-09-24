class Node:
  def __init__(self, val):
    self.data = val
    self.next = None
  
  def getData(self):
    return self.data
  
  def setData(self, val):
    self.data = val
  
  def setNext(self, val):
    self.next = val
  
  def getNext(self):
    return self.next

class LinkedList:
  def __init__(self):
    self.head = None
  
  def isEmpty(self):
    return self.head is None
  
  def add_in_front(self, val):
    new_Node = Node(val)
    new_Node.setNext(self.head)
    self.head = new_Node
  
  def add(self, val):
    new_Node = Node(val)
    if self.head is None:
      self.head = new_Node
    else:
      current = self.head
      while current.getNext() is not None:
        current = current.getNext()
      current.setNext(new_Node)
  
  def size(self):
    length = 0
    current = self.head
    while current is not None:
      length += 1
      current = current.getNext()
    return length
  
  def search(self, item):
    current = self.head
    while current is not None:
      if current.getData() == item:
        return True
      current = current.getNext()
    return False
  
  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while current is not None:
      if current.getData() == item:
        found = True
        break
      previous = current
      current = current.getNext()
    if found:
      if previous is None:
        self.head = current.getNext()
      else:
        previous.setNext(current.getNext())
    else:
      raise ValueError
      print("Value not Found")

  def insert(self, index, val):
    if index > self.size() -1:
      raise IndexError
      print("Index out of bound")
    if index == 0:
      self.add_in_front(val)
    else:
      current = self.head
      new_Node = Node(val)
      previous = None
      position = 0
      while position < index:
        previous = current
        current = current.getNext()
        position += 1
      previous.setNext(new_Node)
      new_Node.setNext(current)
  
  def index(self, val):
    positon = None
    current = self.head
    while current is not None:
      if current.getData() == val:
        return positon
      positon += 1

  def pop(self, index=None):
    if index > self.size() -1:
      print("Index out of bound")
      raise IndexError
    else:
      prev = None
      position = 0
      current = self.head
      while position < index:
        prev = current
        current = current.getNext()
        position += 1
        data = current.getData()
      prev.setNext(current.getNext())
  
  def printList(self):
    current = self.head
    while current is not None:
      print(current.getData())
      current = current.getNext()


ll = LinkedList()
ll.add('i')
ll.add("v")
ll.printList()