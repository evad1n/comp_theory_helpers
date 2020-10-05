#!/usr/bin/env python3

import test_cases as tc
import regular_expressions as rx
import finite_automata as fa
import context_free_grammars as cfg
import push_down_automata as pda

ALPHABET = [('0', '0'), ('0', '1'), ('1', '0'), ('1', '1')]

# FINITE AUTOMATA STATE DIAGRAMS
# The key value for each state defines what possible states can be reached from that particular key
# Start state is always 0
finite_automaton_1 = {
    'states': [
        {('0', '0'): [0], ('0', '1'): [4],
         ('1', '0'): [4], ('1', '1'): [1]},
        {('0', '0'): [4], ('0', '1'): [0],
         ('1', '0'): [2], ('1', '1'): [4]},
        {('0', '0'): [3], ('0', '1'): [4],
         ('1', '0'): [4], ('1', '1'): [2]},
        {('0', '0'): [4], ('0', '1'): [0],
         ('1', '0'): [2], ('1', '1'): [4]},
        {('0', '0'): [], ('0', '1'): [],
         ('1', '0'): [], ('1', '1'): []},
    ],
    'final_states': [0]
}

finite_automaton_2 = {
    'states': [
        {('0', '0'): [1, 2], ('0', '1'): [2],
         ('1', '0'): [2, 3], ('1', '1'): [2, 3, 4]},
        {('0', '0'): [1], ('0', '1'): [], ('1', '0'): [], ('1', '1'): []},
        {('0', '0'): [2], ('0', '1'): [2],
         ('1', '0'): [2, 3], ('1', '1'): [2, 3, 4]},
        {('0', '0'): [4], ('0', '1'): [], ('1', '0'): [], ('1', '1'): []},
        {('0', '0'): [], ('0', '1'): [5], ('1', '0'): [], ('1', '1'): []},
        {('0', '0'): [5], ('0', '1'): [], ('1', '0'): [], ('1', '1'): []},
    ],
    'final_states': [1, 5]
}

# REGULAR EXPRESSIONS
regular_expression_1 = "|(a|b)a*b((b|a(a|b))a*b)*(|a)"
regular_expression_1 = "^(" + regular_expression_1 + ")$"  # Must match whole string

regular_expression_2 = "(a|b)(a|(ba(a|b))*b)" + "(a(a|b)a*b|(ba*b)*)*" + "(a|)|"
regular_expression_2 = "^(" + regular_expression_2 + ")$"  # Must match whole string


# DEFINE LANGUAGE HERE
def language(case):
    """ Test if particular case passes the rules outlined below. Test cases are lists. """
    if not case:
        return True
    top = ''
    bottom = ''
    for step in case:
        top += step[0]
        bottom += step[1]
    return (int(top, 2) * 3) == int(bottom, 2)


def compare_regex_graph(regular_expression, finite_automaton):
    """ Compares a regular expression to a finite automaton for equivalence. """
    for case in tc.cases:
        # Compare regular expression and finite automaton case by case to see if they produce same output
        if rx.did_match(regular_expression, case) != fa.did_complete(finite_automaton, case):
            # Output problem case
            print(f"Failure at case: {''.join(case)}")
            print(f"Regular Expression output: {rx.did_match(regular_expression, case)}")
            print(f"Finite Automaton output: {fa.did_complete(finite_automaton, case)}")
            print("Terminating...")
            return False
    print("Regular Expression is equivalent to Finite Automaton for all test cases!")
    return True


tc.generate_cases(ALPHABET, 5)
print(tc.cases[3])

# ======== CALL FUNCTIONS HERE ========

# compare_regex_graph(pattern_1, graph_1)
# compare_regex_graph(pattern_2, graph_1)
fa.test_finite_automaton(finite_automaton_1, language)


# TODO

# cry
# scream
# cfg
# pda
# cry a lot
# closure operations
# convert to classes?
