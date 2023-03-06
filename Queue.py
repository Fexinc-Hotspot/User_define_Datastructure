#-----------USER_DEFINE DATA STUCTURE------------------

#.QUEUE
#.---Is a linear structure that allow insertion of elements from one end & deletion from others 
#----It follow the rule of FIFO Methodology 

#---The end which allow deletion is know as------------------

#.1******** THE FRONT OF THE QUEUE*********** ---and ------- ***The others end is know as****------

#.2 ********REAR END OF THE QUEUE---------


#--Example
print('-------------------------------------------------------------------------------')
print('A PROGRAM TO PUSH,POPPING & PRINTING HEAD & TAIL BY USING QUEUE DATASTRUCTURE')
print('-------------------------------------------------------------------------------')
print()
queue=['First','Second','Third']
print('1.First we Init....',queue)
print()

#---Pushing Element 

queue.append('Fourth')
queue.append('Fifth')
print('2.Then we push/add two values..... ',queue)
print()

#--Printing head
print('.Sec we print Head of the queue(FIFO)  :',queue[0])
print()

#--printing Tail
n=len(queue)
print('4.Third we print Tail of the queue(FIFO)  :',queue[n-1])
print()

#--Popping the element
queue.remove(queue[0])
print('5.Fifth we popping/removing the value from the queue',queue)
print()