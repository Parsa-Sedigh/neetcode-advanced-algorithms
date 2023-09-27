# Section 3. Tries

## ??-1. Trie
A different kind of tree structure named a trie and another name for it and probably the better name for it is **prefix tree**.

The goal of a prefix tree is to be able to insert word in `O(1)` . By word I mean a string of characters.
When we say O(1) that also could be the size of the word itself, because to insert a word OFC we have to go through every single character of that
word, so maybe a better way to say this is `O(n) where n is the size of the word.`

Usually tries are used for strings of characters, usually not integers and other types of values.

We also want to search for **existence** of a word in O(1) as well. Given some word, we should be able to check does it exist or not in O(1).

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

Insert word: O(1)

Search word: O(1)

Search prefix: O(1)

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

Look at code/3-Tries/??-1-1.py

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

Now let's say we wanna insert the word "ape". curr is set to root, we're gonna go character by character in the word "ape", now is "a" a child of
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

## ??-2. Union Find
## ??-3. Segment Tree
## ??-4. Iterative DFS