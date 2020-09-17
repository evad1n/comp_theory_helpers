import itertools

cases = []

def generate_combinations(alphabet, digits):
    """Performs the cartesian product on an array with itself {digits} number of times"""
    yield from itertools.product(*[alphabet], repeat=digits) 

def generate(alphabet, max_digits):
    """Generates 2^(MAX_DIGITS) of test cases from given alphabet"""
    cases.clear()
    for digits in range(0, max_digits+1):
        for case in generate_combinations(alphabet, digits):
            cases.append(''.join(case))