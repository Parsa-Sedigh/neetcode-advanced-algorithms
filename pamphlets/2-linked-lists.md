## 6-1. Fast and Slow Pointers (Floyd's tortoise and hare)
tortoise is the slow pointer and hare is the fast pointer.

Another two pointer algo, this time for linked lists.

The naive way for 6-1-1.py: count the length of the linked list. Then in the next pass, go till the middle.

If the num of nodes is even, let's consider the second one in the middle as the answer.

T: O(n)

---

Second solution: it's still O(n).

When we say reach the end of the linked list, it means the fast pointer is **either** at the last node or it's None(out of bounds).

Q: Now if the fast pointer travelled the entire length of the linked list, how far did the slow pointer travel(given it's travelling
half as fast as the fast pointer)?

A: the slow pointer would've travelled half the length of the LL. That means by the time the fast pointer reaches the
end of the LL, the slow pointer should be at the middle of the LL. This works when we have a linked list with odd length.
If we had a LL of even length, it's still at the midway, because we defined the second node as being the middle, when we have
a LL with even length.

Q: But what if in a even len LL, we defined the first node of the middle to be the answer?

A: in the beginning of the algo, we would initialize the slow at the head and fast at the next node.

Fast and slow pointers can be used for cycle detection in a LL.

One way to detect that is using some hashing DS, like hashset. If we were told that the val of each node is unique, we can
add that to hashset. We might not be guaranteed that, so another way is to save the pointer to every node to the hashset.
Then if we ever visit the same node twice, we would see that's already added to the hashset, so we can detect we have a cycle.

But we get extra memory with this approach.

- T: O(n)
- M: O(n)

To eliminate the extra memory we can use fast and slow pointer. 

Each iteration of loop has a unique color in the img:
![](../img/2-linked-lists/6-1-1.png)

The fast and slow pointers intersect at node 5.

Q: Why is it that if the fast and slow pointers intersect, that implies that the linked list has a cycle?

A: The fast pointer should always be ahead of the slow pointer. But if we have a cycle, that's the only way the slow pointer
would be able to catch up with the fast pointer(it's actually reverse! the fast pointer will catch up with the slow).
But if our LL didn't have cycle, the fast would always be twice as far ahead of the slow pointer.

Note: If we do have a cycle, it's **guaranteed** that they're gonna intersect. Why? Because the fast pointer is going twice as
fast.

When we have a cycle, fast is moving 2 spaces and slow with 1 space. At each iteration, the distance between them should be shrinking
by one(in the cycle).

**The intersection is guaranteed to happen in O(n). Because in the cycle, the distance from the fast to the slow can't possibly be
longer than the length of the cycle.**

So if the length from the fast to the slow in the cycle is m, it takes m iterations of the loop for the pointers to be
at the same place(intersect). In other words, by the time slow pointer enters the cycle(since there might be some nodes
before reaching the cycle), the slow pointer won't have to traverse longer than the length of the cycle until meeting the
fast pointer. So m is not more than the length of the cycle.
So the slow pointer will only have to iterate through the entire length of the linked list. The fast pointer will have to
iterate through two times that. So we could say overall time complexity is `O(2*n)` where n is the length of the entire LL.
So it's O(n).

So that's why this is O(n) algo. Because the slow pointer won't possibly have to iterate through longer than the entire LL, the
fast pointer have to do twice that much.

Note: The fast and slow pointers don't necessarily intersect at the beginning(head) of the cycle.

So the slow pointer won't go through multiple laps of the cycle.

---

6-1-3.py:

The fast and slow pointers won't necessarily intersect at the beginning of the cycle.

To solve this, we initialize another slow pointer at the head of the LL. Now after fast and slow intersected, we don't care
about the fast pointer anymore. Move the slow pointer and also the second slow pointer. We're guaranteed that the slow and 
the second slow pointer intersect at the start of the cycle.

Q: Why the second slow pointer and slow pointer meet at the head of the cycle?

A: Let's call the portion before the head of the cycle, p. This portion can be 0(length can be 0). Let's call the length of the cycle is
called c. Call the length from the beginning of the cycle to the point of intersection, c - x. So the remaining of the
cycle is x:

![](../img/2-linked-lists/6-1-2.png)

So x is the distance from the intersection until the beginning of the cycle.

The distance that the slow pointer have to travel is: `p + c - x`. The fast pointer will go through p and an entire loop of the cycle and
then also c - x. So: `p + c + c - x`. And we know in terms of distance: slow * 2 = fast.
So we have: 2 * (p + c - x) = p + c + c - x => p - x = 0 => `p = x`.

So x which is the distance from the intersection until the beginning of the cycle, is equal to p which is the distance from
the start of the LL until the start of cycle.

So when two slow pointers intersect, they will see each other at the head of the cycle.