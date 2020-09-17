# Functions to test Finite Automata state diagrams
from test_cases import cases


def next_states(path, next, graph):
    """ Calculates all possible next states for this graph given current path and next character. """
    newPaths = []
    # Get current state
    current = path[-1]
    # Generate all possible new paths given the current path
    for option in graph['states'][current][next]:
        newPaths.append(path + [option])
    return newPaths

def did_complete(graph, case):
    """ Returns True if this case ended on a final state for this graph. """
    # Start state is always 0
    paths = [[0]]
    # For each character in the length of the test case
    for i in range(len(case)):
        # Get next character to process
        next_char = case[i]
        newPaths = []
        # Generate new possible states from current states
        for path in paths:
            newPaths += (next_states(path, next_char, graph))
        # Overwrite old states with the new states
        paths = newPaths[:]
    # Check to see if this case ends on a final state
    for path in paths:
        if path[-1] not in graph['final_states']:
            return False
    return True

def test_graph(graph, in_langauge):
    """ Returns True if the graph satisfies all test cases. """
    for case in cases:
        # Compare graph output with expected output from language
        if did_complete(graph, case) != in_langauge(case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Graph output: {did_complete(graph, case)}")
            print(f"Should have been: {in_langauge(case)}")
            print("Terminating...")
            return False
    print("Graph recognizes language for all test cases!")
    return True


def compare_graphs(graph_1, graph_2, in_langauge):
    """ Returns True if the two graphs are equivalent for all test cases. """
    for case in cases:
        # Compare each graph case by case to see if they produce same output
        if did_complete(graph_1, case) != did_complete(graph_2, case):
            # Output problem case
            print(f"Failure at case: {case!r}")
            print(f"Graph 1 output: {did_complete(graph_1, case)}")
            print(f"Graph 2 output: {did_complete(graph_2, case)}")
            print("Terminating...")
            return False
    print("Graphs are equivalent for all test cases!")
    return True