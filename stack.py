#---------USER_DEFINED DATASTRUCTURE---------

#.2 STACK

#---Stack is the linear structure that allow to inser and removed from the same End  
#---Eg:(LIFO) System.Insertion and deletion is known as push() and pop()

#Example
print('-----------------------------------------------------------')
print('A PROGRAM THAT PUSH,POP & PRINT THE TOP VALUE FROM THE STACK')
print('------------------------------------------------------------')
print()

stack=['first','second','third']
print('First we init..',stack)
print()

#----Push the Element
stack.append('fourth')
stack.append('fifth')
print('Sec we push two Element :',stack)
print()

#----Printing Top
n=len(stack)
print('We printing Top value of the Stack :',stack[n-1])
print()

#---popping Element
stack.pop()
print(stack)
print()# the print() method it gives space btn line & line
