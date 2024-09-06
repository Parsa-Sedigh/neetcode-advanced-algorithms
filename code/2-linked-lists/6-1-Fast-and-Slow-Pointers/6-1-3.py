# Q: Determine if a linked list contains a cycle and return the beginning of the cycle, otherwise return null.

# T: O(n)
# M: O(1)
def cycleStart(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # did we reached the end of the list?
    if not fast or not fast.next:
        return None

    slow2 = head

    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next

    return slow