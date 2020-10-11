#!/usr/bin/env python3

import test_cases as tc
import regular_expressions as rx
import finite_automata as fa
import context_free_grammars as cfg
# import push_down_automata as pda

ALPHABET = ['0', '1']

# FINITE AUTOMATA STATE DIAGRAMS
# The key value for each state defines what possible states can be reached from that particular key
# Start state is always 0
finite_automaton_1 = {
    'states': [
        {'0':[4], '1':[1]},
        {'0':[5], '1':[2]},
        {'0':[6], '1':[3]},
        {'0':[7], '1':[3]},
        {'0':[8], '1':[5]},
        {'0':[9], '1':[6]},
        {'0':[10], '1':[7]},
        {'0':[11], '1':[7]},
        {'0':[8], '1':[9]},
        {'0':[9], '1':[10]},
        {'0':[10], '1':[11]},
        {'0':[11], '1':[11]},
    ],
    'final_states': [11]
}

finite_automaton_2 = {
    'states': [
        {'0':[2,6], '1':[1,5]},
        {'0':[2], '1':[1]},
        {'0':[3], '1':[1]},
        {'0':[3], '1':[4]},
        {'0':[], '1':[]},
        {'0':[6], '1':[5]},
        {'0':[6], '1':[7]},
        {'0':[6], '1':[8]},
        {'0':[9], '1':[5]},
        {'0':[6], '1':[10]},
        {'0':[6], '1':[11]},
        {'0':[11], '1':[11]},
    ],
    'final_states': [0,1,2,3,11]
}

# REGULAR EXPRESSIONS
regular_expression_1 = "(..0)(((..)(....)*0)|((....)+1))"
regular_expression_1 = "^(" + regular_expression_1 + ")$"  # Must match whole string

regular_expression_2 = "(a|b)(a|(ba(a|b))*b)" + "(a(a|b)a*b|(ba*b)*)*" + "(a|)|"
regular_expression_2 = "^(" + regular_expression_2 + ")$"  # Must match whole string

# CONTEXT FREE GRAMMARS
cfg_1 = {
    'variables': {
        'A': ['1A1', '0A0', 'B'],
        'B': ['CCC'],
        'C': ['0', '1'],
    },
    'terminals': ['0', '1'],
    'start': 'A'
}

# DEFINE LANGUAGE HERE
def language_1(case):
    """ Test if particular case passes the rules outlined below. Test cases are lists. """
    if len(case) % 2 == 1 or len(case) < 6:
        return False
    left = case[:len(case)//2]
    right = case[len(case) // 2 :]
    
    return left[2] == '0' and ((right[-1] == '0' and len(right) % 2 == 1) or (right[-1] == '1' and len(right) % 2 == 0))

def language_2(case):
    """ Test if particular case passes the rules outlined below. Test cases are lists. """
    if len(case) % 2 == 0:
        return False
    z_start = (len(case) // 2) - 1
    z_end = (len(case) // 2) + 2
    left = case[:z_start]
    right = case[z_end :]
    z = case[z_start:z_end]
    if len(z) < 3:
        return False
    reversed = left[:]
    reversed.reverse()
    # print(left, z, right, reversed == right)
    return reversed == right


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


tc.generate_cases(ALPHABET, 10)

# ======== CALL FUNCTIONS HERE ========

# compare_regex_graph(pattern_1, graph_1)
# compare_regex_graph(pattern_2, graph_1)
# fa.test_finite_automaton(finite_automaton_1, language)
rx.test_regex(regular_expression_1, language_1)
cfg.test_context_free_grammar(cfg_1, language_2, 12)
