# Section 1. Arrays

## 1-0. Kadanes Algo
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

Better way: Detecting duplicates is sth that can be improved with hash tables. Look at `2-1-2.py`.

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
## 5-4. Prefix Sums