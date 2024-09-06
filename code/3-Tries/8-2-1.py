class UnionFind:
    # n is the size of the set(number of nodes in the graph which might have disconnected components)
    # T: O(n)
    # M: O(n)
    def __init__(self, n):
        self.par = {}

        # by rank we mean height. We want the height of our trees to be as small as possible. That makes find() method more efficient.
        self.rank = {}

        # for each node we wanna keep track of what it's parent and rank is. We do it with hashmap but we can do it with an arr as well,
        # specially if we were given a range of vals, like 1-4, we could use an arr for par and rank fields.
        # Note: The rank of non-root nodes of trees are irrelevant, because we won't use them to union their tree with another tree.
        # We only use the rank of root nodes.
        for i in range(1, n + 1):
            # initially, the parent of a node is itself.
            self.par[i] = i

            # Note: We could initialize the rank as 1 as well. That depends on do you consider the height of a single node
            # as 0 or 1. Though this doesn't really matter as long as you're consistent because it's all about COMPARING
            # of ranks(heights).
            self.rank[i] = 0

    # Given node n, we wanna find it's ROOT parent.
    # T:
    # - O(n) - if neither path compression and union by rank is used.
    # - O(log(n)) - if one of them is used
    # - O(1) if both are used
    # M: O(1)
    def find(self, n):
        p = self.rank[n]

        # keep traversing to the parent until curr node is the same as it's parent. Because we know when we hit a node
        # that it's parent is itself, that node doesn't have any more parents, so we can stop there.
        while p != self.par[p]:
            # What we do here is called "path compression". It's an optimization.
            # As we're moving forward towards the root, SIMULTANEOUSLY we can also shorten the paths and this action won't
            # affect the time complexity of the find() method. So why we shouldn't do it? It's good to do it because
            # it doesn't hurt the time complexity(won't make this method slower). This is an optimization that
            # will help us if we ever wanted to run find() on the same node again.
            # Here, as we move forward, we're setting the parent of cur node to be it's grand parent! Cause that will
            # shorten the chain, so that later, we would have to traverse a shorter path on the same node again.
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    # we wanna union two nodes together to form a single set
    # T:
    # - O(n) - if neither path compression and union by rank is used.
    # - O(log(n)) - if one of them is used
    # - O(1) if both are used
    # M: O(1)
    def union(self, n1, n2):
        # find the root node of n1 and n2 and union those nodes together
        p1, p2 = self.find(n1), self.find(n2)

        # if the root parent of n1 and n2 is the same, don't do anything, we can't perform a union. Return False to indicate
        # union was not successful. n1 and n2 are already a part of the same set(tree), they are already connected.
        if p1 == p2:
            return False

        # The time of rest of the method is: T: O(1). The bottleneck is coming from the find().

        # instead of all these blocks, we could arbitrarily only say: self.par[p2] = p1
        # But that wouldn't always be efficient. Instead, we wanna union by rank(height).
        # Note: If the heights were different, doing a union op is not gonna affect the height. Because if we
        # connect the smaller root, the height of the larger tree won't change.
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            # if the heights are the same, we arbitrarily pick one of the root nodes and make it the child of the other.
            # When we do this, ONLY ONE edge is gonna be added to the new set. Therefore it's height is only
            # change by 1.
            self.par[p1] = p2
            self.rank[p2] += 1

        return True
