# This python program makes it easy to test Finite Automata state diagrams

# Added NFA/DFA graph comparison for equivalence >>>>

# The graph data structure
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
        {0:[1], 1:[3]},
        {0:[4], 1:[2]},
        {0:[0], 1:[2]},
        {0:[3], 1:[3]},
        {0:[4], 1:[2]},
    ],
    'final_states': [0,2,4]
}

# DEFINE LANGUAGE HERE
def is_valid(case):
    """Test if particular case passes the rules outlined below. Test cases are strings."""
    return case.count('0') % 2 == 0 and case.count('1') % 2 == 1 and '01' not in case


def next_states(pattern, step, graph):
    """Calculates all possible next states given current pattern and next step"""
    newPatterns = []
    start = pattern[-1]
    for option in graph['matrix'][start][step]:
        newPatterns.append(pattern + [option])
    return newPatterns

def did_complete(graph, case):
    """Returns whether this case ended on a final state for this graph"""
    # First graph
    patterns = [[0]]
    # For each step in the length of the test case
    for i in range(len(case)):
        # step becomes the next digit to process
        step = case[i]
        newPatterns = []
        # Generate new possible states from old possible states
        for pattern in patterns:
            newPatterns += (next_states(pattern, int(step), graph))
        patterns = newPatterns[:]
    # Check to see if this case ends on a final state
    complete = False
    for pattern in patterns:
        if pattern[-1] in graph['final_states']:
            complete = True
    return complete

def test_graph(cases):
    """Returns True if the graph satisfies all test cases. There will be 2^(MAX_DIGITS) of test cases."""
    # Generate all combinations from test language up to combinations with MAX_DIGITS (digits == characters in this case)
    for case in cases:
        # Get case output for primary graph
        if not is_valid(case) == did_complete(primary_graph, case):
            print(f"Failure at case: {case!r}")
            print(f"Regex output: {did_match(pattern, case)}")
            print(f"Should have been: {is_valid(case)}")
            print("Terminating...")
            return False
    print("Graph produces correct output for all cases!")
    return True


def compare_graphs(cases):
    """Compares two DFA/NFA to determine if they are equivalent"""
    # Generate all combinations from test language up to combinations with MAX_DIGITS (digits == characters in this case)
    for case in cases:
        # Compare each graph case by case to see if they produce same output
        if did_complete(primary_graph, case) != did_complete(compare_graph, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Regex output: {did_match(pattern, case)}")
            print(f"Should have been: {is_valid(case)}")
            print("Terminating...")
            return False
    print("Graphs are equivalent for all cases!")
    return True