# check if an array(or string, because their problems are solved the same way) is a palindrome
# Q: Given a string of characters, return true if it's palindrome, return false otherwise: O(n)
def isPalindrome(word):
    L, R = 0, len(word) - 1

    # if the pointers ever cross each other(meaning L is not less than R anymore), that means we checked every single pair of
    # chars and therefore the input is a palindrome.
    while L < R:
        if word[L] != word[R]:
            return False

        L += 1
        R -= 1

    return True