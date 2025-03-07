def isPalindromeReverse(s):
    """
    Checks if a given string is a palindrome by reversing it and comparing with the original.

    Time Complexity: O(n)
        - The preprocessing (cleaning) takes O(n) time.
        - `s[::-1]` creates a reversed version of the string, which takes O(n) time.
        - The comparison `s == s[::-1]` takes O(n) in the worst case.
        - Overall complexity: O(n).


    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    reversed_s = s[::-1]  # Reverse the string
    return s == reversed_s  # Compare original and reversed string