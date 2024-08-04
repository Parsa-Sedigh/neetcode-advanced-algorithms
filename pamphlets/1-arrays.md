# Section 1. Arrays

## 1-0. Kadanes Algo
This algo has overlap with a lot of algos like two-pointers and sliding window(they're kinda techniques), DP and greedy.

This algo is technically a DP and greedy algo.

1-0-1.py: Brute force way is to find all the sub-arrays. To get every sub-array starting at the first position and going forward,
it's gonna be O(n) where n is the size of the arr. And to do the same exact thing starting from the second position
and going forward, it would also be O(n). So T: O(n^2) .

Note: Always `check if the prev curr is less than 0 and set it to 0` before doing anything else.

### Kadanes algo
**Is used to find the maximum sum subarray from a given array.**

![](../img/1-arrays/1-0-1.png)

We can call the subarr, a window.

### Sliding window variation of Kadanes algo
At some point, our window slides to begin in the position where 3 lives. And then it grew to include 3 and 4.
![](../img/1-arrays/1-0-2.png)

Note: All the values in the window, represent `curSum`.

## 2-1. Sliding Window Fixed
**Q:** Given an array, return true if there are two elements within a window of size k that are equal.

Within a window of size k means that the window can be **at most** of length k(elements have to be in different positions, so not an
element with itself!).

**Brute force way:** Look at every window of size k. In this approach, we use two pointers where left pointer would represent the beginning
of our window and our right pointer(R) should never be at the same position as our L pointer because otherwise we would compare the
element to itself and say we found equal values but they're not two different values. So the R pointer always starts at L + 1.

In `2-1-1.py` the outer loop is gonna run as many times as how many elements we have in the array. The inner loop is gonna run roughly 
k - 1 times.

Time: O(n * k) which for large windows is not good.

A common technique with sliding window problems: `min(len(nums), L + k)` when looping. It's because when we don't have enough elements to
have our window. So we would consider the end of the array as last element. So we won't go out of bounds of array.

Better way: **Detecting duplicates is sth that can be improved with hash tables.** Look at `2-1-2.py`.

Now, instead of comparing the current value to all of the window which before was of O(n) , we use a hash table and say: `if nums[R] in window`
which is a constant time operation(O(1)).

With this approach, we won't be worry about small size windows as well, it's handling this case well.

## 3-2. Sliding Window Variable
**Q:(2-1-4)** Find the length of the longest subarray, with the same value in each position.

The L and R pointers in this **can** be at the same position because it's a valid window.

This problem(`2-1-3`) is actually simple enough that we don't need the sliding window(at least we don't explicitly need a left and a right pointer).
We're just using L and R in `2-1-3` to see the main idea of sliding window.

More complicated sliding window:

**Q:(2-1-4)** Find the minimum length subarray, where the sum is greater than or equal to the target. **Assume all values are positive.**

Brute force way is to find all the possible sub arrays.

Since all the elements are positive, when we have a window that has total sum of equal or greater than the target, by growing the window again, it's not
gonna ever get smaller to reach that target again. So when we reach that target, we need to shrink our window so that we can again have a valid
window(can have a total sum equal or larger than the target), so we will increment the `L` pointer, but this incrementing won't necessarily be done
only once, because if we just increment it by 1, we couldn't see all the possible minimum lengths. So the L pointer could be incremented multiple times while
the R pointer is pointing to the same index. **But the time complexity would still be O(n) !**
Why? 

Normally when we have two nested for loops, we think that is always O(n^2), but in this case it's not! Because that inner loop is not always going to
execute. The inner loop runs a **total of n times and not n times for each iteration of the outer loop** , but n times total. So even though we have
two nested loops, the time complexity is still O(n). 

Note: When we shrink the window by incrementing the `L` pointer, the total sum would become smaller OFC.

So when we have a variable-length window, we usually have an inner while loop but that doesn't mean the time complexity is O(n^2) .

## 4-3. Two Pointers
Sliding window is pretty much a subset of two-pointers.

Q: What is the difference of two-pointers and sliding window problems?

A: With two pointer algos, we care mostly about the two individual els that the pointers are pointing at.
But in sliding window, we care about the entire window.

In 4-3-1.py, one solution is build another arr by iterating the original arr in reverse order.
But another way that doesn't have extra memory is with two pointers.

So in this technique, we usually initialize two pointers at the end of the arr and then we start moving them towards each other
based on some condition until they meet or cross each other.

## 5-4. Prefix Sums
Prefix means that we're starting at the beginning.

So the prefix of this arr: [2, -1, 3, -3, 4] is any subarr(typically any **contiguous** sub arr) that **starts at the beginning of the arr**.
Some examples are: [2], [2, -1], [2, -1, 3] and ... . Note: The entire arr itself is a prefix.

But [-1, 3] is not a prefix because it doesn't start at the beginning. Also [2, 3] is not a prefix typically because it typically
it should be contiguous.

We don't have to get the res of previous prefix sums. It's repeated work. At each step, we know the prev prefix sums, so we don't have
to recompute them again.

We can also have prefix products and ... .

**Note: Given an arr of n els, we can have n^2 sub-arrs.**

Postfix: Every subarr starting at the end.

We use prefix and postfix to eliminate repeated work.

`5-4-1.py`: 

A naive way to solve it, is not worrying about prefixes, just go through L to R and calc sum. In worst case: T: O(n) .

But this can be done more efficiently. Let's say we have: rangeSum(1, 3). None of the prefix sums will give us the sum
from index 1 to 3(because they start from beginning), but we can use prefix sum till index 3 and subtract the prefix sum of
index 0 to get sum of index 1 to 3.

Another ex: to get sum of 3 to 4, we say: rangeSum(4) - rangeSum(2):

Note: The green numbers are prefix sums up until that index.
![](../img/1-arrays/5-4-1.png)

Since we pre-computed the prefix sums, everytime we're asked the sum(product, ...) of any arbitrary subarr, we can get it in
O(1).

So we pre-compute the work using prefix sums and then we don't need to do those works again.

Note: We can solve this problem using postfix sums.

In PrefixSum DS, we're assuming we're gonna be calling rangeSum() very frequently and we're not gonna be calling the constructor
very frequently(since it's T is O(n)). That's why solving the sum problem with prefix is more efficient because we're assuming
we're gonna be calling rangeSum() more frequently than constructor.