def isPalindromePointers(s):
    """
    Checks if a string is a palindrome using pointers to compare characters from both ends.

    Time Complexity: O(n), where n is the length of the string.
        - Cleaning the string (removing non-alphanumeric characters and converting to lowercase) takes O(n).
        - Comparing characters from both ends requires at most n/2 iterations, resulting in O(n).

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(cleaned_string) - 1

    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1

    return True
