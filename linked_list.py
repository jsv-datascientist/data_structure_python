class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#as in Leetcode
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def add_first(self, val):
        newNode = Node(val)
        newNode.next = self.head #assign the address to the next value is 1024 

        self.head = newNode

    def add_last(self, val):
        newNode = Node(val)

        if (self.head == None):
            self.head = newNode
        else:
            lastNode = self.head
        
        while (lastNode.next):
            lastNode = lastNode.next
        
        lastNode.next = newNode

    
    def search( self, key):
        temp = self.head 

        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    
    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next 

        else:
            temp = self.head 
            while temp.next != None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next

'''
slow fast pointer 
slow move by 1 and fast by 2, if they meet at anypoint together 
we have cycle. 

This can be done using hashset but timecompleisty is 
'''
def hasCycle(self, head : Node) -> bool:
    slow, fast = head, head 

   #while fast is not null and fast.next is not null
   # else it is at end of list 
    while fast and fast.next:
        slow = slow.next # move by 1
        fast = fast.next.next # move by 2 

        if slow == fast:
            return True 
    else: False


'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

def addTwoNumber(self, l1: List, l2:list):
    pass



'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


         1    2 3 4 null
  prev  curr
'''
def reverse_linked_list (self, head):
    """
    :type head : [LinkedList]
    :rtype : [LinkedList]
    """

    prev, current = None, head

    while current:
        temp_current_next = current.next 

        #move the null pointer so this is befining now
        current.next = prev 

        #move the pointers 
        prev = current 
        current = temp_current_next


    return prev


def deleteDuplicates(head):
    dummy = ListNode(0)  # Create a dummy node
    dummy.next = head
    prev = dummy  # Use `prev` to link non-duplicate nodes

    current = head
    while current:
        # Check for duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            while current.next and current.val == current.next.val:
                current = current.next
            # Link `prev` to the node after the duplicates
            prev.next = current.next
        else:
            # Move `prev` forward only if `current` is not a duplicate
            prev = prev.next
        current = current.next  # Move `current` forward

    return dummy.next



'''
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

no of times to rotate would be (length - k - 1)
when the k = length of linked list, then there is no change in llist 

in case if the k > length, do k = k % length that many times need to move 
'''
def rotate_linkedlist(self, head:ListNode) -> ListNode:
    #when the list is empty 
    if not head :
        return head 
    
    #get the length of the linked list 

    length, tail = 1, head
    while tail.next:
        tail = tail.next 
        length += 1

    #if K is greater than length 
    k = k % length 

    if k == 0:
        return head 
    
    #move to the pivot 
    #current is at the point of breat
    current = head 
    for i in range (length -k-1):
        current = current.next 
    
    #3 4-5, 4 is gng to be new head 
    newHead = current.next 
    
    #rotate 
    current.next = None #set 3 to none
    tail.next = head
    
    return newHead



if __name__ == "__main__":
    llist = LinkedList()

    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)


    llist.head.next = middle
    middle.next = last

    llist.printLinkedList()

