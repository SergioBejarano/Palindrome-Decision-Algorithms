import unittest
from algorithms.isPalindromeDeque import isPalindromeDeque
from algorithms.isPalindromePointers import is_palindromePointers
from algorithms.isPalindromeSubstrings import isPalindromeSubstrings

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

    def test_palindromes_deque(self):
        for s in self.palindromes:
            self.assertTrue(isPalindromeDeque(s))
        for s in self.non_palindromes:
            self.assertFalse(isPalindromeDeque(s))

    def test_palindromes_pointers(self):
        for s in self.palindromes:
            self.assertTrue(is_palindromePointers(s))
        for s in self.non_palindromes:
            self.assertFalse(is_palindromePointers(s))

    def test_palindromes_substrings(self):
        for s in self.palindromes:
            self.assertTrue(isPalindromeSubstrings(s))
        for s in self.non_palindromes:
            self.assertFalse(isPalindromeSubstrings(s))

if __name__ == "__main__":
    unittest.main()
