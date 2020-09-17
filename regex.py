# Functions to test regular expressions
import re
from test_cases import cases


def did_match(pattern, case):
    """ Returns True if regex matched for this case. """
    if re.match(pattern, case):
        return True
    return False

def test_regex(pattern, in_language):
    """ Returns True if regex recognizes language. """
    for case in cases:
        # Should it have matched?
        if in_language(case) != did_match(pattern, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Regex output: {did_match(pattern, case)}")
            print(f"Should have been: {in_language(case)}")
            print("Terminating...")
            return False
    print("Regex recognizes the language correctly!")
    return True

def compare_regex(pattern_1, pattern_2, in_language):
    """ Returns True if the two regular expressions are equivalent for all test cases. """
    for case in cases:
        # Compare each regex case by case to see if they produce same output
        if did_match(pattern_1, case) != did_match(pattern_2, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Regex 1 output: {did_match(pattern_1, case)}")
            print(f"Regex 2 output: {did_match(pattern_2, case)}")
            print("Terminating...")
            return False
    print("Regular expressions are equivalent for all cases!")
    return True