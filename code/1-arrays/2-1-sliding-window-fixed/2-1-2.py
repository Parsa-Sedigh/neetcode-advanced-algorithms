# Same problem using sliding window technique.
# T: O(n)
# M: O(k) - The space complexity is O(k), where k is the size of the window. This is because the window
# set can hold at most k elements at any time.
def closeDuplicates(nums, k):
    window = set()  # cur window of size <= k
    L = 0

    for R in range(len(nums)):

        # if our window is greater than k:
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True

        window.add(nums[R])

    return False
