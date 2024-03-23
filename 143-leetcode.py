# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        headd = head
        head = head.next
        fsnode = headd
        ls = []

        while head != None:
            if head.next != None:
                print(head.val)
                templl = copy.deepcopy(head)
                templl.next = None
                ls.append(templl)
            else:
                fsnode.next = head
                fsnode = fsnode.next
                while len(ls) > 0:
                    fsnode.next = ls.pop(0)
                    fsnode = fsnode.next
                    if len(ls) > 0:
                        fsnode.next = ls.pop(-1)
                        fsnode = fsnode.next
                    
                
                head = headd  
                break
                
            
            head = head.next
            
        return head



        
