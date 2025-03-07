def isPalindromeRecursiveHelper(s):
    """
    Recursively checks if a cleaned string is a palindrome.

    Args:
        s (str): The cleaned string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    length = len(s)
    if length == 0 or length == 1:
        return True
    if s[0] != s[length-1]:
        return False
    return isPalindromeRecursiveHelper(s[1:length-1])

def isPalindromeRecursive(s):
    """
    Recursively checks if a given string is a palindrome.

    Time Complexity: O(n)

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    return isPalindromeRecursiveHelper(cleaned_string)
