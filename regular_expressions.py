# Functions to test regular expressions
import re
from test_cases import cases


def did_match(regular_expression, case):
    """ Returns True if regular expression matched for this case. """
    # re.match returns 'None' if not matched so we cannot return it directly
    if re.match(regular_expression, ''.join(case)):
        return True
    return False


def test_regex(regular_expression, language):
    """ Returns True if regular expression recognizes language for all test cases. """
    for case in cases:
        # Should it have matched?
        if did_match(regular_expression, case) != language(case):
            # Output problem case
            print(f"Failure at case: {''.join(case)}")
            print(f"Regex output: {did_match(regular_expression, case)}")
            print(f"Should have been: {language(case)}")
            print("Terminating...")
            return False
    print("Regex recognizes the language for all test cases!")
    return True


def compare_regex(regular_expression_1, regular_expression_2, language):
    """ Returns True if the two regular expressions are equivalent for all test cases. """
    for case in cases:
        # Compare each regex case by case to see if they produce same output
        if did_match(regular_expression_1, case) != did_match(regular_expression_2, case):
            # Output problem case
            print(f"Failure at case: {''.join(case)}")
            print(f"Regular Expression 1 output: {did_match(regular_expression_1, case)}")
            print(f"Regular Expression 2 output: {did_match(regular_expression_2, case)}")
            print("Terminating...")
            return False
    print("Regular expressions are equivalent for all test cases!")
    return True
