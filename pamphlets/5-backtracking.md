## 5-1. Subsets
Combinatorics subject is usually applied to backtracking problems. One common one is subsets which is the simplest one.

Distinct subset means: If we include [1, 2], we can't include [2, 1]. So just because orders are different, doesn't mean
they're different subsets. That would be a **permutation**.

Since we're given a list of **distinct** numbers as input, we don't have to worry about getting duplicate subsets.

For every one of the items in the input, we have a choice to include it or not in the subset. It sounds like a decision tree!

In the img, the left child of root is when we chose to include 1 and the right child is when we chose not to include the 1.
So the left subtree is all the subsets with 1 and the right subtree is all the subsets with 1.
Then in the left child of [1] node, we chose to include 2(which resulted in [1, 2]) and for it's right child, we
chose not to include 2(resulted in [1]).

We have 8 subsets.

**The number of subsets is always gonna be the same and it's: `2^n` where n is number of els in the input.**
Because for each one of the els in the input arr, we have two choices of either including it or not. So in the above example:
2 * 2 * 2 = 2^3 = 8.

Time complexity:

Q: Does that mean that 2^n is also the worst time complexity? Because 2^n is how many subsets we have to generate.

A: No. Because for every single subset(one element of the result arr), we have to build it. Each one of the subsets is gonna be
a separate arr itself. We can't just reuse the work we did for every one of them. Our returning result is gonna be a big list
of lists. One of them is gonna be of size n, but most of them are gonna be smaller than size n, but we're gonna proximate
that each of them is gonna be of size n in worst case. So we have 2^n subsets and each of them is size n, so: `T: O(n * 2^n)`.

Space complexity: O(n * 2^n) is technically the space complexity as well. Because that's the space it takes to contain the result.
But typically when talking about space complexity, we don't include the space it takes to contain the result. So if we're not
including the resulting arr of arrays, the space would be the height of the decision tree which is h and in this case it's n.
So `M: O(n)`.

![](../img/5-backtracking/5-1-1.png)

In problems like ??-1-2, backtracking and sometimes other types, but usually with backtracking problems, we wanna sort the
input arr. Because first of all, we know that the time complexity for generating all distinct subsets is gonna be O(2^n * n).
So sorting(O(n* log(n))) is not gonna be expensive and it makes these problems easier.

We can't use the same idea that we used for prev question where for every single el, we chose whether we wanna include it
or not. That's not gonna result in distinct subsets if we have duplicates in the input arr.

We're gonna take advantage of sorting the input arr. Since the arr is sorted, we know that all duplicates are gonna be adjacent
to each other.

Note: We can use both twos in a single path, but we can't use them in two branches.

We want this path to represent all subsets that don't include any 2s.
![](../img/5-backtracking/5-1-2.png)

What about it's left path? Is that path gonna include both of the 2s? Not necessarily, but it's gonna contain at least
one 2. So it's gonna be distinct from it's right path.

How did we achieve this?

When choosing what to choose, first we make the decisions on that el(decide to choose and decide not to choose - 2 branches).
Then we go to a loop to move forward until the next el is different than what we're currently at.

Note the incomplete decision tree is:

![](../img/5-backtracking/5-1-3.png)