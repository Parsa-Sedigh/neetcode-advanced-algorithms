# Section 3. Tries

## 7-1. Trie
A different kind of tree structure named a trie and another name for it and probably the better name for it is **prefix tree**.

A trie is a tree and each node can have up to 26 children(a-z).

The goal of a prefix tree is to be able to insert word in `O(1)` . By word I mean a string of characters.
When we say O(1) that also could be the size of the word itself, because to insert a word OFC we have to go through every single character of that
word, so maybe a better way to say this is `O(n) where n is the size of the word.`

Usually tries are used for strings of characters, usually not integers and other types of values.

**We also want to search for existence of a word in O(1) as well. Given some word, we should be able to check does it exist or not in O(1).**

Q: Now you might think: Can't both of these operations most easily be achieved using a hashset?

A: Yes, but there's one last operation that a hashset can't get for us and that is **search prefix**.

Maybe the most important operation is being able to search for a prefix. That's why we call this a prefix tree.

With a hashmap, we can't search for prefixes. For example given a prefix of "ap", we wanna know are there any words in our prefix tree
with this prefix? With a prefix tree, we would be able to return true in O(1) (**actually in O(<size of the prefix itself like "ap">)**).
But with a hashmap, there's no easy way to do this, we would in the worst case have to go through every single string in the hashmap.
So this was the problem we're trying to solve with prefix tree.

### Application
An application for prefix tree would be with search engines or any kind of searching at all. For example when you use google search and
you start typing a few characters and it auto completes or it gives you a few suggestions, it essentially uses a prefix tree. It uses
the prefix that you typed in and it checks what strings match that prefix.

- Insert word: O(1)
- Search word: O(1)
- Search prefix: O(1)

Note: These three ops are actually: **O(<size of the word which is constant>)**

A trie is a tree of characters. So each node is going to be a character and the most common restriction specially for coding interviews
is that we only have to worry about lowercase letters `a-z`, but even if we had a larger character set, it wouldn't make a huge difference
in the structure.

`a-z` gives us 26 characters. In that case, we would have a tree that looks like the img below. You can think of it as having a single
root node that's empty. Or maybe a better way to think about it would be we have 26 root nodes in this case. One for each character
that we're worrying about(in case of a-z, 26). What that means is that all the words that start with 'a', are gonna go down the subtree
under 'a'. Now that 'a', is gonna have all words that start with 'a'. So the 'a' root, is gonna have at most 26 children(a-z) and each of
those 26 children are also going to have at most 26 children again. It might be that some nodes don't have any children at all.

Let's say we're looking for the word apple, we would want to go to the branch that has 'a', then we go to the child of a that is p
and then we go to the child of p that has value of p and ... . If at anypoint of this traversing, we don't have the character that we're looking
for, then we know for sure, we can't possibly contain the word apple, because this is where it would be if we had inserted it, but it's not here.
So we have not inserted the word apple.

Since each node could have 0-26 children(in this case), it doesn't make sense to give every single node a left and right pointer, an easier
way to do this would be a hashmap. So every node is going to have a value(the character) but also a hashmap of all of it's children and the key
of that hashmap is going to be some character from a-z. So each character is gonna map to some node.

![](../img/3-Tries/%3F%3F-1-1.png)

Notice how the TrieNode class doesn't store any characters. We could store a character in each node if we wanted to, but it's redundant because
you can see in Trie class.

Let's say we want to insert the word "apple". How would the insert algo work?

First in our root node which is sorta an empty node.

Inserting:

For example we wanna insert the word "apple". We go through every single char in the word and starting from the root of the trie,
we check if it has the char "a", if it has, we don't do anything and move our curr pointer to "a" which is the child of the root node.
But if the root node didn't have the "a" char at it's hashmap of children, we insert it and then move the curr pointer to child "a".
So the curr pointer would be shifted to the new node that we just inserted. Now we go to the next character "p". If there isn't a child
with the key "p" in the hashmap of "a", we insert "p" as a key with value of TrieNode in the hashmap of "a" and update the curr to point
to "p" now and go to the next character which is again "p".

At the end of the algo, is for the last character(at that point, we have a pointer to that last char), we want to mark it as the end of a word.
So: `self.word = True`.

![](../img/3-Tries/%3F%3F-1-1.png)

Search for a word:

Similar to inserting a word.

The search method runs in O(1) or maybe O(n) if n is the size of the word. This is the same for `insert` and `startsWith`.

Note: In search, when we iterated through every character in the word that we're searching for and the iteration is done, now can we immediately
return true? No. We're gonna return whether this last character is the end of a word or not and we have marked that character as the end of a word,
so we return true.

But let's say we were looking for the word "a"?

Start at the root, does it have a child "a"? Yes, now curr would point to that child. Now we're at the end of the word, now we return
`return curr.word`. That child was never marked as the end of a word. So we would return false. The word "a" does not exist in our prefix tree
and that makes sense because just because we inserted the word apple, doesn't mean we inserted the word "a" or the word "ap" or "app" or every prefix
of "apple" word. That's why everytime we insert a word completely, we mark the last character as the end of a word, because then when we search
we don't wanna say that "ap" is a word(in the case we inserted the word "apple"), we never inserted "ap", we inserted apple.

So every prefix is not necessarily a word.

Now let's say we wanna insert the word "ape". `curr` is set to root, we're gonna go character by character in the word "ape", now is "a" a child of
the root, it is, so we don't have to insert a new "a" as the child of root. We don't want redundant nodes, we don't need two "a"s that are
both children of the root. Because we want all words that start with "a", to go down the branch of "a"(child of root). We don't want to have to
search two branches or multiple branches for the current character, we just want a single branch to be able to search for.

Now we go to the next character "p". We see that's also already been inserted as the child of "a", now "e". That has not been inserted as child of 
p(look at the img), so add it and mark it as the end of a word.

Note: End of the words are marked as green.

startsWith

Note: The main purpose of this DS is startsWith method.

This method doesn't necessarily take a word, it takes a prefix and we wanna return true if there's any words that start with this prefix.

---

A trie can be helpful for searching for prefixes. It's also efficient for inserting and searching for words.

![](../img/3-Tries/%3F%3F-1-2.png)

## 8-2. Union Find data structure(Disjoint sets DS)
It's technically a tree DS, but it's mostly applied to generic graphs. So it can get complicated but the implementation is easy.

Suppose we have a graph but it has disjoint sets(in pic, we have 2 disjoint sets). The entire graph is not connected.
We're used to deal with connected graphs like trees where every node is connected.
![](../img/3-Tries/8-2-1.png)

The strength of union find DS is dealing with disjoint sets where we can have one or more connected components.
The strengths of union find is to count the number of connected components.

It can also be used for cycle detection:
![](../img/3-Tries/8-2-2.png)

Note: DFS algo can also be used for cycle detection with the same time complexity. But sometimes union find is more efficient
and sometimes it's required.

**EX:** We're given a list of edges like: [[1, 2], [4, 1], [2, 4]] and number of nodes is 4. Determine if this graph
has cycle or not. Note: Each given edge is undirected. So [1, 2] means 1 and 2 nodes point at each other.

Answer: Union find is a forest of trees which means we have a bunch of trees. Now we wanna initialize the given edges.
For this, we have a tree for every single disjoint set. Initially, we assume that all nodes are disjoint sets.
Initially, we don't know any info about the nodes.

For each node, we store what is the parent of that node. Initially, all nodes don't have a parent. But an easier way to
to do that is to say that the node itself is it's own parent. But we could say at the beginning that it doesn't have a parent.

Now when we wanna connect two nodes like [1, 2] or in other words, we wanna union 1 and 2 together. 
We **arbitrary(in some cases it does matter which one is chosen as child)** 
set one node as the child of the other. For example, we set 2 as the child of 1. So now 2 has a parent which is 1:
![](../img/3-Tries/8-2-3.png)

Now we wanna union the current tree with [2, 4]. We can make 4 to be the child of 2. Or we can make 2 be child of 4, but
2 already has a parent. So we can't do this. So we can't arbitrary pick in this case. The best way to get around this issue
is instead of unioning the two nodes themselves, first we go to the last parent of the node and arrive in the root
node of the current tree, which in our case is 1, and then we union the roots of the trees of the two nodes that we wanted
to union.

**So instead of unioning the nodes themselves, we union the root parents of the tree that they're in.**
So in this case, is it better to make 1 as the child of 4(the right tree in pic):
![](../img/3-Tries/8-2-4.png)

or make 4 as child of 1:
![](../img/3-Tries/8-2-5.png)

Which one is better?

The second one is more balanced. But why being balanced is important?
Because when we're trying to union two nodes together, first we wanna find the **root** parent of those two nodes. Then
we union those two disjoint sets together so that they form a single set. If we have a balanced tree then the 
"find root parent" op is gonna be more efficient to traverse than having an unbalanced tree(resembling a linked list).

This op is called `union by rank(height)`. So we take the height of the trees that we're unioning and take that into
consideration. We **could** do it arbitrary if we wanted to, but it's more efficient when we union by height.
We take the tree with smaller height and add it as a child of the root node of the larger tree. So we connected the 
tree with less height to the **root** of the tree with larger height because that makes it more efficient to find the root
from the nodes(because we would traverse less to get to root), we could connect it to the children of larger tree,
but that would be less efficient later to get to the root.

So until now, using union find, we have a tree(graph) on the left instead of having a graph like the red one:

So union find doesn't necessarily accurately represent the graph because as you see the 2 and 4 nodes are not directly
connected as given in the edges list. Union find is about being able to detect cycles and count the number of connected components.
![](../img/3-Tries/8-2-6.png)

Now we wanna do: [4, 1] edge. That means we wanna find the root parent of the node 4 and root parent of node 1. **The roots
of both nodes is the same. This means these two nodes are part of the same connected component.** That means we can't union these.
They're already a part of the same set. We can return some val to indicate we were not able to union, for example False.
That would indicate these two nodes are already connected and that would indicate that the given graph has a cycle.
Because we're connecting two nodes that were already connected. Note: We're assuming that all given edges were unique.
Given this assumption that all edges are different and the fact that we were connecting two nodes that were already 
connected, it means we must have a cycle.

The real graph with the given edges is(the one that we drew a line around):
![](../img/3-Tries/8-2-7.png)

Our graph has a cycle.

---

A visualization of path compression:
![](../img/3-Tries/8-2-8.png)

Here, we ran find() on 5, we wanna shorten the path of 5 to it's root. So as we move forward, we set the parent of the node
to it's grand parent so later, we will traverse a shorter path if we ever ran find() on the same node again.

So this op doesn't make the find() op more efficient **the first time**, but if we ever ran find() on the same node again,
it will be more efficient.

Note: This action is not always required in union find.

---

### time and space

In naive case where we don't use path compression and we don't use union by rank in union(), the find() method
will be O(n). Because we might have a unbalanced tree like it resembles a linked list. So traversing it up from
the leaf node(worst case) would be O(n). We can make this better to O(log(n)) by just doing one of the two
optimizations. We can either use path compression which is just a single line of code and make
find() on average to be T: O(log(n))
Or we can decide to use union by rank which will also make the time to be O(log(n)) for find because doing
that will result in having a more balanced tree(since the height of the tree would be smaller).

But if we implement **both** path compression and union by height, we get a complicated math func which is written like:
`ɑ * n` which is read as `alpha times n` and is called **inverse ackermann** function and this function reduces to
`O(1)` even for really large n values, it will usually be O(1), not literally O(1) but it can be simplified to O(1) in most cases.

But the find() method is gonna run multiple times. In our example, it would run for the number of edges that we have(2 times
number of edges), let's say the number of edges is `m`. So in general the time complexity of union find, if we have
m edges, is: `O(m * log(n))`. But if we use both path compression and union by rank, the time of union find would be: `O(m)`.
This is why **in some cases union find is more efficient than a DFS for cycle detection or counting the number of connected components.**

So for our example:
- T: O(m)
- M: O(n)

## 9-3. Segment Tree
## 10-4. Iterative DFS