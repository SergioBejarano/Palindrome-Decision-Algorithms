import time
import pandas as pd
from algorithms.isPalindromeReverse import isPalindromeReverse
from algorithms.isPalindromePointers import isPalindromePointers
from algorithms.isPalindromeRecursive import isPalindromeRecursive

def measure_execution_time(algorithm, test_string):
    """
    Measures the execution time of a palindrome checking algorithm.

    :param algorithm: Palindrome function.
    :param test_string: String to be checked.
    :return: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(test_string)
    return time.time() - start_time

def gather_execution_times(string_sizes):
    """
    Collects execution times for different string sizes.

    :param string_sizes: List of string sizes to test.
    :param samples_per_size: Number of samples per size.
    :return: Pandas DataFrame with execution times.
    """
    results = []

    for size in string_sizes:
        print(f"Computing size {size}")

        times_reverse = []
        times_pointers = []
        times_recursive = []

        test_strings = [
                        "ab" * size,                                        # Alternating pattern
                        "a" * size,                                         # Single repeating character
                        "racecar" * size,                                   # Repeated palindrome
                        "abcdefgh" * size,                                  # Random non-palindrome pattern
                        "A" * (size // 2) + "B" + "A" * (size // 2),        # Symmetric large palindrome
                        "level" * (size // 2),                              # Repeated short palindrome
                        "abcddcba" * (size // 2)                            # Structured palindrome
                    ]
        for test_string in test_strings:
            times_reverse.append(measure_execution_time(isPalindromeReverse, test_string))
            times_pointers.append(measure_execution_time(isPalindromePointers, test_string))
            #times_recursive.append(measure_execution_time(isPalindromeRecursive, test_string))


        results.append({
            'Size': size,
            'Reverse': sum(times_reverse) / len(test_strings),
            'Pointers': sum(times_pointers) / len(test_strings),
            #'Recursive': sum(times_recursive) / len(test_strings)
        })

    return pd.DataFrame(results).groupby("Size", as_index=False).mean()
