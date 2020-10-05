# Functions to test finite automata
from test_cases import cases


def next_states(path, next, finite_automaton):
    """ Returns all possible next states for this finite automaton given current path and next character. """
    new_paths = []
    # Get current state
    current = path[-1]
    # Generate all possible new paths given the current path
    for option in finite_automaton['states'][current][next]:
        new_paths.append(path + [option])
    return new_paths


def did_complete(finite_automaton, case):
    """ Returns True if this case ended on a final state for this finite automaton. """
    # Start state is always 0
    paths = [[0]]
    length = len(case)
    # For each character in the length of the test case
    for i in range(length):
        # Get next character to process
        next_char = case[i]
        new_paths = []
        # Generate new possible states from current states
        for path in paths:
            new_paths += (next_states(path, next_char, finite_automaton))
        # Overwrite old states with the new states
        paths = new_paths[:]
    # Check to see if this case ends on a final state
    for path in paths:
        if len(path) == length + 1 and path[-1] in finite_automaton['final_states']:
            return True
    return False


def test_finite_automaton(finite_automaton, in_langauge):
    """ Returns True if the finite automaton satisfies all test cases. """
    for case in cases:
        # Compare finite automaton output with expected output from language
        if did_complete(finite_automaton, case) != in_langauge(case):
            # Output problem case
            print(f"Failure at case: {case}")
            print(f"Finite Automaton Output: {did_complete(finite_automaton, case)}")
            print(f"Should have been: {in_langauge(case)}")
            print("Terminating...")
            return False
    print("Finite Automaton recognizes language for all test cases!")
    return True


def compare_finite_automata(finite_automaton_1, finite_automaton_2, in_langauge):
    """ Returns True if the two finite automata are equivalent for all test cases. """
    for case in cases:
        # Compare each finite automaton case by case to see if they produce same output
        if did_complete(finite_automaton_1, case) != did_complete(finite_automaton_2, case):
            # Output problem case
            print(f"Failure at case: {case}")
            print(f"Finite Automaton 1 output: {did_complete(finite_automaton_1, case)}")
            print(f"Finite Automaton 2 output: {did_complete(finite_automaton_2, case)}")
            print("Terminating...")
            return False
    print("Finite Automata are equivalent for all test cases!")
    return True
