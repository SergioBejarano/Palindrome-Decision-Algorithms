import unittest
from algorithms.isPalindromeReverse import isPalindromeReverse
from algorithms.isPalindromePointers import isPalindromePointers
from algorithms.isPalindromeRecursive import isPalindromeRecursive

class TestPalindromeAlgorithms(unittest.TestCase):
    def setUp(self):
        self.palindromes = [
            "A man a plan a canal Panama",
            "Was it a car or a cat I saw",
            "No 'x' in Nixon",
            "Eva, can I see bees in a cave?",
            "Do geese see God?",
            "Never odd or even",
            "Madam, in Eden, I'm Adam",
            "Able was I, I saw Elba",
            "",  # Empty string
            "a"  # Single character
        ]

        self.non_palindromes = [
            "Hello, World!",
            "Python is fun",
            "This is not a palindrome",
            "OpenAI is great",
            "Artificial Intelligence",
            "Palindrome check fails here"
        ]

    def test_palindromes_Reverse(self):
        self.assertTrue(isPalindromeReverse(self.palindromes[0]))
        self.assertTrue(isPalindromeReverse(self.palindromes[1]))
        self.assertTrue(isPalindromeReverse(self.palindromes[2]))
        self.assertTrue(isPalindromeReverse(self.palindromes[3]))
        self.assertTrue(isPalindromeReverse(self.palindromes[4]))
        self.assertTrue(isPalindromeReverse(self.palindromes[5]))
        self.assertTrue(isPalindromeReverse(self.palindromes[6]))
        self.assertTrue(isPalindromeReverse(self.palindromes[7]))
        self.assertTrue(isPalindromeReverse(self.palindromes[8]))
        self.assertTrue(isPalindromeReverse(self.palindromes[9]))

        self.assertFalse(isPalindromeReverse(self.non_palindromes[0]))
        self.assertFalse(isPalindromeReverse(self.non_palindromes[1]))
        self.assertFalse(isPalindromeReverse(self.non_palindromes[2]))
        self.assertFalse(isPalindromeReverse(self.non_palindromes[3]))
        self.assertFalse(isPalindromeReverse(self.non_palindromes[4]))
        self.assertFalse(isPalindromeReverse(self.non_palindromes[5]))

    def test_palindromes_pointers(self):
        self.assertTrue(isPalindromePointers(self.palindromes[0]))
        self.assertTrue(isPalindromePointers(self.palindromes[1]))
        self.assertTrue(isPalindromePointers(self.palindromes[2]))
        self.assertTrue(isPalindromePointers(self.palindromes[3]))
        self.assertTrue(isPalindromePointers(self.palindromes[4]))
        self.assertTrue(isPalindromePointers(self.palindromes[5]))
        self.assertTrue(isPalindromePointers(self.palindromes[6]))
        self.assertTrue(isPalindromePointers(self.palindromes[7]))
        self.assertTrue(isPalindromePointers(self.palindromes[8]))
        self.assertTrue(isPalindromePointers(self.palindromes[9]))

        self.assertFalse(isPalindromePointers(self.non_palindromes[0]))
        self.assertFalse(isPalindromePointers(self.non_palindromes[1]))
        self.assertFalse(isPalindromePointers(self.non_palindromes[2]))
        self.assertFalse(isPalindromePointers(self.non_palindromes[3]))
        self.assertFalse(isPalindromePointers(self.non_palindromes[4]))
        self.assertFalse(isPalindromePointers(self.non_palindromes[5]))

    def test_palindromes_Recursive(self):
        self.assertTrue(isPalindromeRecursive(self.palindromes[0]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[1]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[2]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[3]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[4]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[5]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[6]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[7]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[8]))
        self.assertTrue(isPalindromeRecursive(self.palindromes[9]))

        self.assertFalse(isPalindromeRecursive(self.non_palindromes[0]))
        self.assertFalse(isPalindromeRecursive(self.non_palindromes[1]))
        self.assertFalse(isPalindromeRecursive(self.non_palindromes[2]))
        self.assertFalse(isPalindromeRecursive(self.non_palindromes[3]))
        self.assertFalse(isPalindromeRecursive(self.non_palindromes[4]))
        self.assertFalse(isPalindromeRecursive(self.non_palindromes[5]))

if __name__ == "__main__":
    unittest.main()
