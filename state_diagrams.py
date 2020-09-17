# Functions to test Finite Automata state diagrams
from test_cases import cases


def next_states(pattern, next, graph):
    """ Calculates all possible next states given current pattern and next character for a graph. """
    newPatterns = []
    start = pattern[-1]
    for option in graph['states'][start][next]:
        newPatterns.append(pattern + [option])
    return newPatterns

def did_complete(graph, case):
    """ Returns True if this case ended on a final state for this graph. """
    # Start state is always 0
    patterns = [[0]]
    # For each character in the length of the test case
    for i in range(len(case)):
        # step becomes the next character to process
        next_char = case[i]
        newPatterns = []
        # Generate new possible states from old possible states
        for pattern in patterns:
            newPatterns += (next_states(pattern, next_char, graph))
        patterns = newPatterns[:]
    # Check to see if this case ends on a final state
    complete = False
    for pattern in patterns:
        if pattern[-1] in graph['final_states']:
            complete = True
    return complete

def test_graph(graph, in_langauge):
    """ Returns True if the graph satisfies all test cases. """
    # Generate all combinations from test language up to combinations with MAX_DIGITS (digits == characters in this case)
    for case in cases:
        # Get case output for primary graph
        if not in_langauge(case) == did_complete(graph, case):
            print(f"Failure at case: {case!r}")
            print(f"Graph output: {did_complete(graph, case)}")
            print(f"Should have been: {in_langauge(case)}")
            print("Terminating...")
            return False
    print("Graph produces correct output for all cases!")
    return True


def compare_graphs(graph_1, graph_2, in_langauge):
    """ Returns True if the two graphs are equivalent for all test cases. """
    # Generate all combinations from test language up to combinations with MAX_DIGITS (digits == characters in this case)
    for case in cases:
        # Compare each graph case by case to see if they produce same output
        if did_complete(graph_1, case) != did_complete(graph_2, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Graph 1 output: {did_complete(graph_1, case)}")
            print(f"Graph 2 output: {did_complete(graph_2, case)}")
            print("Terminating...")
            return False
    print("Graphs are equivalent for all cases!")
    return True