# Q: determine if a linked list has a cycle

# T: O(n)
# M: O(1)
def hashCycle(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False