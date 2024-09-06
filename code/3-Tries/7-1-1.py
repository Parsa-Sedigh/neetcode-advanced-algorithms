class TrieNode:
	def __init__(self):
		# We're talking about 26 characters(a-z), so we could've defined an array of size 26 for children, but a hashmap makes it
		# a lot more flexible. That's why it would be easy to handle A-Z as well or maybe any type of alphabet that we needed to
		self.children = {} # hashmap

		# For every node, we're also gonna have a boolean value to determine if this character is the end of a word or not.
		self.word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	# T: O(L)
	# M: O(L)
	def insert(self, word):
		curr = self.root

		# we want to start going through every character in this input word(like apple) and we wanna
		# insert every single character into the trie. But note if the current character of word has not already been inserted into the trie,
		# then we insert that character, otherwise, we don't insert it again. If we don't use this check, we would overwrite the
		# children property of cur in the next iterations which would cause loosing data.
		for c in word:
			if c not in curr.children: # T: O(1)
				# T: O(1)
				curr.children[c] = TrieNode()

			curr = curr.children[c]

		curr.word = True

	# T: O(L)
	# M: O(1)
	def search(self, word: str) -> bool:
		curr = self.root

		for c in word:
			if c not in curr.children:
				return False

			curr = curr.children[c]

		return curr.word

	# T: O(L)
	# M: O(1)
	def startsWith(self, prefix: str) -> bool:
		curr = self.root

		for c in prefix:
			if c not in curr.children:
				return False

			curr = curr.children[c]

		return True