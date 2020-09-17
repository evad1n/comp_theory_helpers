import re

from test_cases import cases


# DEFINE LANGUAGE HERE
def is_valid(case):
    """Test if particular case passes the rules outlined below. Test cases are strings."""
    return case.count('1') % 2 == 0

def did_match(pattern, case):
    if re.match(pattern, case):
        return True
    return False

def test_regex(pattern):
    """Returns True if regex recognizes language"""
    for case in cases:
        # Should it have matched?
        if is_valid(case) != did_match(pattern, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Regex output: {did_match(pattern, case)}")
            print(f"Should have been: {is_valid(case)}")
            print("Terminating...")
            return False
    print("Regex recognizes the language correctly!")
    return True

def compare_regex(pattern_1, pattern_2):
    """Compares two regular expressions to determine if they are equivalent"""
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