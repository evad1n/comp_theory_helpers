import test_cases
import regex
import state_diagrams

ALPHABET = "01" # just translate any binary ALPHABET (such as 'ab') into "01" because it is easier

# FINITE AUTOMATA STATE DIAGRAMS
# The key value for each node defines what possible nodes can be reached from that particular key
primary_graph = {
    'matrix': [
        {0:[1], 1:[1]},
        {0:[1], 1:[2]},
        {0:[0], 1:[1]},
    ],
    'final_states': [0,2]
}

compare_graph = {
    'matrix': [
        {0:[1], 1:[2]},
        {0:[4], 1:[]},
        {0:[4], 1:[2]},
        {0:[4], 1:[]},
        {0:[4], 1:[5]},
        {0:[], 1:[5]},
    ],
    'final_states': [5]
}

# REGULAR EXPRESSIONS
pattern = "(0|11*)00*11*"
pattern = "^(" + pattern + ")$" # Must match whole string

# DEFINE LANGUAGE HERE
def is_valid(case):
    """Test if particular case passes the rules outlined below. Test cases are strings."""
    return case.count('1') % 2 == 1

def compare_regex_graph(pattern, graph):
    """Compares a regular expression to a graph for equivalence"""
    for case in test_cases.cases:
        # Compare graph and regex case by case to see if they produce same output
        if state_diagrams.did_complete(graph, case) != regex.did_match(pattern, case):
            # Output problem case
            print(f"Failure at case: {case!r}\nTerminating...")
            return False
    print("Regex is equivalent to graph for all cases!")
    return True

test_cases.generate(ALPHABET, 10)

# test_regex(pattern)

compare_regex_graph(pattern, compare_graph)

print(state_diagrams.did_complete(compare_graph, '01101'))

print(regex.did_match(pattern, '01101'))





""" TODO
-> implement alphabet keys for full range of alphanumeric values
-> fix module structure for centralized testing
 """