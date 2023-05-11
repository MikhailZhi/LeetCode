# version 1
# solution for usual list
li = input('l= ')
list=[]
for i in li:
    if i != "," and i!=" ":
        list.append(i)


if len(list)%2 == 0:
    start = int(len(list)/2)
    end = len(list)
    print(list[start:end])
else:
    start = int(len(list)//2)
    end = len(list)
    print(list[start:end])    

# version 2
# а решение было нужно для связных списков
# solution from chat gpt

class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
                
        def middleNode(head: ListNode) -> ListNode:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        return middleNode(head)

# version 3
# solution from leetcode

# Time Complexity :  O(n)
# Space Complexity : O(1)
class Solution(object):
    def middleNode(self, head):
        # We need two pointers, one is head with one step each iteration, and the other is tmp with two steps each iteration.
        temp = head
        while temp and temp.next:
            # In each iteration, we move head one node forward and we move temp two nodes forward...
            head = head.next
            temp = temp.next.next
        # When temp reaches the last node, head will be exactly at the middle point...
        return head
