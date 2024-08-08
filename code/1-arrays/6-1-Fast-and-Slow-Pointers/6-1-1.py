# Q: Find the middle of a linked list

# T: O(n)
# M: O(1)
def middleOfList(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow