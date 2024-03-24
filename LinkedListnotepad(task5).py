class Node: #node for single linked list
    def __init__(self,data):
        self.data=data
        self.next=None
class DNode:# node for doublelinkedlist
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linkedlist(): #creating and inserting elements in the linkedlist
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):#inserting elements in the linked list
        newnode=Node(data)
        if self.head==None: # if the single linked list is empty we do this operation
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
    def show(self): #to print elements in the linked list or we can say to print elements in the notepad
        current=self.head
        while current:
            print(current.data)
            current=current.next
class Doublelinkedlist():#creating and inserting elements into the doublelinked list
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):#inserting notes refrences(addresses) into the double linked list
        newnode=DNode(data)
        if self.head==None: # if the double linked list is empty we do this operation
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail.next.prev=self.tail
            self.tail=newnode
    def show(self): #to print elements in the double linked list 
        current=self.head
        while current:
            print(current.data)
            current=current.next
def open(d,flag):# to navigate doublelinked list to select the notepad you want to open
    i=1
    temppage=d.head
    print('type: "next" to turn to next page, "prev" to previous page ,"select" to print the page, "page" to view the page number')
    while 1:# loop to navigate to next and previous notepads as many times we want to
        pageop=input()
        if pageop=='next':#goes to next notepad
            if i+1<=pages:
                i+=1
                temppage=temppage.next
                print('note no :{}'.format(i))
            else:#the next operation failed because we did not created that many notepads
                print('u did not creat that many pages,NexT operation Failed')
        elif pageop=='prev':
            if i-1>0:
                i-=1
                temppage=temppage.prev
                print('note no :{}'.format(i))
            else:#the prev operation failed because its going below zero
                print('u r going below first page ,PreV operation Failed')
        elif pageop=='select':#to select that notepad
            if flag==1: # i use this to return the address of the notepad for edit,search,copypaste functions 
                return temppage.data
            print('---------------------------------Note :{} -----------------------------------'.format(i))#if we are not using edit,search,copypaste function
            temppage.data.show()                                                                            #then we can just print the notepad
            print('-----------------------------------------------------------------------------')
            break
        elif pageop=='page':#to view the current notepad number we are on
            print('note no:',i)
        else:
            print('invalid input!')
def edit(d):# to edit the line in notepad
    print('which note do u want to edit')
    flag=1 #we use this to get the address of that node that we want to edit
    tempnodeofdll=open(d,flag)
    temphead=tempnodeofdll.head
    flag=0#revert it to zero
    eop=input('which operation u want to choose: "insert" to insert "delete" to delete a line" "modify" to modify a line  : ')
    if eop=='insert':
        prev=None
        p=1
        while temphead:
            print('do you want to insert it as line no:  |{}| "yes" or press enter'.format(p))
            iop=input()
            if iop=='yes':
                newnode=Node(input('enter your line:'))
                if prev:
                    prev.next=newnode
                else:
                    tempnodeofdll.head=newnode
                newnode.next=temphead
                return
            prev=temphead
            temphead=temphead.next
            p+=1
    elif eop=='delete':
        prev=None
        while temphead:
            print('do you want to delete this line:|| {} || "yes" or press enter'.format(temphead.data))
            dop=input()
            if dop=='yes':
                if prev:
                    prev.next=temphead.next
                else:
                    tempnodeofdll.head=tempnodeofdll.head.next
                print('line:"{}" is deleted '.format(temphead.data))
                return
            prev=temphead
            temphead=temphead.next
    elif eop=='modify':
        while temphead:#loop to know which line u want to edit
            print('do you want to edit this line? type "Yes" else press enter: ',temphead.data)
            eornot=input()
            if eornot=='Yes':#if Yes we edit that line by takign new input to that line 
                print('type the line')
                editline=input()
                temphead.data=editline
            temphead=temphead.next
    else:
        print('INVALID INPUT')
def search(d):# to search the element in the notepad
    print('which note do u want to search')
    flag=1#same as above to get the address of that notepad 
    tempnodeofdll=open(d,flag)
    temphead=tempnodeofdll.head
    flag=0#revert the flag to zero
    j=1#to count the page numbers
    print('which word u want to find:')
    searchword=input()
    while temphead:#to check everyline till we found the specified element
        if searchword in temphead.data:
            print('the word is in line no :{}  and the line is : {}'.format(j,temphead.data))
            choice=input('end the search or continue? "End" to end Else press enter\n\n')#we can continue to search if there are more 
            if choice=='End':#to end the search
                return
        j+=1
        temphead=temphead.next
    print('No more specified elements found')#prints if there are no elements like that
def copyandpaste(d):#to copyandpaste line from one notepad to anothernotepad
    print('which note do u want to copy from')
    flag=1#same logic as above
    tempnodeofdll=open(d,flag)
    temphead=tempnodeofdll.head
    flag=0#reverting value
    while temphead:#loop to select which line you want to copy
        print('do you want to copy this line? type "Yes" else press enter: ',temphead.data)
        eornot=input()
        if eornot=='Yes':
            print('Copied!')
            tempcopy=temphead.data
            print('where do you want to paste this?')
            flag=1#same logic
            tempnodeofdll=open(d,flag)
            temphead2=tempnodeofdll.head
            flag=0#same logic
            while temphead2:#loop to select at which place u want to replace
                print('do you want to replace : "{}"  with the copied one'.format(temphead2.data))
                tinput=input('press "Yes" to paste else press enter')
                if tinput=='Yes':#to confirm u want to paste there
                    temphead2.data=tempcopy
                temphead2=temphead2.next
        temphead=temphead.next
n=Linkedlist() #creating object of single linked list
d=Doublelinkedlist() #creating object of doublelinkedlist
pages=0
while 1: #loop to select an operation multiple times
    print('select an operation: "create" to create new note,  "open" to open notes,  "edit" to edit a note, "search" to search the word , "copy" to copy and paste\n')
    op=input()
    if op=='create':# to create notepad
        print('type "ExiT" to exit document"\n')
        while 1:
            x=input()
            if x=='ExiT':
                break
            n.insert(x)
        temp=n
        print('do you want to save?:type "Save" else press enter')
        sav=input()
        if sav=='Save': #saves the refrence of the notepad that we created in double linked list
            print('SAVED!')
            d.insert(temp)
            pages+=1
        else:
            print('did not Saved.')
        n=Linkedlist() #creating new object or we can say refreshing with new address
    elif op=='open': #to open the notepad by using doublelinkedlist
        if pages<=0:
            print('you have not created any notes.')
        else:
            open(d,0)
    elif op=='edit':#to edit the notepad
        edit(d)
    elif op=="search":#to search the specified word in the notepad 
        search(d)
    elif op=="copy":#to copy a line from one notepad to another notepad 
        copyandpaste(d)
    else:
        print('invalid input')

    


