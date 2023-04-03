# find the length of longest subarray with the same value in each position: O(n)
def longestSubarray(nums):
    # current longest length
    length = 0
    L = 0

    """
    Keep increasing the window(R moving forward) until we get to a point where we can't grow it anymore and at that point we start shrinking
    our window from left side.
    """
    for R in range(len(nums)):

        """
        When we encounter an element that is not equal to our window elements(which all have the same value equal to nums[L]),
        we want to shrink the window to the right side. But we don't need to just increment L just 1 step. We can skip all the elements
        in window and directly assign R to L(L and R at the same point and then again start looking for bigger windows).
        Why? Because we know if we just encounter a new value that all the other values of window are not equal, we can immediately set
        L to where R points(we calculated the size of window so we don't want to work on smaller windows, let's just set L = R).
        BTW it doesn't change time complexity. So we won't need an inner loop.     
        """
        if nums[L] != nums[R]:
            L = R

        # size of the current window is R - L + 1
        length = max(length, R - L + 1)

    return length
