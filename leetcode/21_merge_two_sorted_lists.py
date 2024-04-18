class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
    output = ListNode()
    while list1 and list2:
        output.next = max(list1.val, list2.val)

    if list1:
        output.next = list1
    elif list2:
        output.next = list2

    return output
        

