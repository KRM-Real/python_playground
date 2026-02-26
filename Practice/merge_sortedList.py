# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

def mergeTwoLists(list1, list2):

    merged_list = list1 + list2

    return sorted(merged_list)
    
list1 = [1,2,3,0,0,0]
list2 = [2,5,6]
print (mergeTwoLists(list1,list2))