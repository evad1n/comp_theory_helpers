from itertools import product

cases = []

def generate_cases(alphabet, max_digits):
    """ Generates 2^(max_digits + 1) of test cases from given alphabet. """
    cases.clear()
    for digits in range(0, max_digits+1):
        for case in product(alphabet, repeat=digits):
            cases.append(list(case))
