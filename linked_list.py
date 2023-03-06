
#-----------USER_DEFINED DATASTRUCTURE-------------------

#.1 LINKED LIST
#-----Is a linear data structure ,in which element are not stored at contiguos memory location
#------The element in a linked list are linked using pointers

#---Example
#---First the program will print list value
print('-----------------------------------------------')
print('--LINKED LIST PROGRAM ON HOW ITS WORKS--')
print('-----------------------------------------------')
IList=['First','Second','Third']
print('First we init...:',IList)

print()

#---Second when the program run/excuted the it will add new record fourth,fifth etc by using apend function
#----Adding Element by using append Method
# & is used to add element to the End of the list

IList.append('Fourth')
IList.append('Fifth')
IList.insert(3,'sixth')#----Insert function method is used to insert value to the specied position

print('Sec we add three items :',IList)
print()

#--Third it will remove the second values by using remove function

IList.remove('Second')
print('Third we Remove Seoc Item  :',IList)
print()

#---That is how Linked_list work in program 