# Q: given a list of distinct nums, return all possible distinct subsets.

# T: O(n * 2^n)
# M: O(n)
def subsetsWithoutDuplicates(nums):
    subsets, curSet = [], []

    # Note: When passing arrs, we're not creating a new var every time we call helper(). We're passing a reference to the
    # same var. We're reusing the curSet and subsets throughout the algo.
    helper(0, nums, curSet, subsets)

    return subsets

def helper(i, nums, curSet, subsets):
    # we could use = here as well.
    if i >= len(nums):
        # The subset copying curSet.copy() takes O(k) time where k is the current length of curSet.
        # In the worst case, k can be n.
        subsets.append(curSet.copy())

        return

    # Note: Think having a DFS.
    # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)

    # undo the work we did previously(which was appending nums[i]), since we wanna try the right subtree which is not including
    # the current nums[i].
    curSet.pop()

    # decision NOT to include nums[i]
    helper(i + 1, nums, curSet, subsets)