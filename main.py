import test_cases
import regex
import state_diagrams

ALPHABET = "ab"

# FINITE AUTOMATA STATE DIAGRAMS
# The key value for each state defines what possible states can be reached from that particular key
# Start state is always 0
graph_1 = {
    'states': [
        {'0':[1], '1':[1]},
        {'0':[1], '1':[2]},
        {'0':[0], '1':[1]},
    ],
    'final_states': [0,2]
}

graph_2 = {
    'states': [
        {'a':[0], 'b':[1]},
        {'a':[1], 'b':[0]},
    ],
    'final_states': [1]
}

# REGULAR EXPRESSIONS
pattern_1 = "a*b(a|ba*b)*"
pattern_1 = "^(" + pattern_1 + ")$" # Must match whole string

pattern_2 = "a*b(a|ba*b)*"
pattern_2 = "^(" + pattern_2 + ")$" # Must match whole string

# DEFINE LANGUAGE HERE
def language(case):
    """ Test if particular case passes the rules outlined below. Test cases are strings. """
    return case.count('b') % 2 == 1

def compare_regex_graph(pattern, graph):
    """ Compares a regular expression to a graph for equivalence. """
    for case in test_cases.cases:
        # Compare regex and graph case by case to see if they produce same output
        if regex.did_match(pattern, case) != state_diagrams.did_complete(graph, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Regex output: {regex.did_match(pattern, case)}")
            print(f"Graph output: {state_diagrams.did_complete(graph, case)}")
            print("Terminating...")
            return False
    print("Regex is equivalent to graph for all test cases!")
    return True

test_cases.generate_cases(ALPHABET, 10)

# ======== CALL FUNCTIONS HERE ========

# regex.test_regex(pattern, language)

# state_diagrams.test_graph(graph_2, language)

# compare_regex_graph(pattern, primary_graph)
