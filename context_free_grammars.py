#!/usr/bin/env python3

# Functions to test context free grammars
from test_cases import cases, generate_cases


cfg_1 = {
    'variables': {
        'A': ['0B0', '1B1', 'C'],
        'B': ['BB', 'C'],
        'C': ['0', '1', ''],
    },
    'terminals': ['0', '1'],
    'start': 'A'
}

def language(case):
    """ Test if particular case passes the rules outlined below. Test cases are lists. """
    return case == [] or case[0] == case[-1]

def transition(string, cfg):
    """ Returns a list of strings with each string representing a possible transition from the original string. """
    new = []
    for index, char in enumerate(string):
        # If it's a variable
        if char in cfg['variables']:
            for possible in cfg['variables'][char]:
                new.append(string[0:index] + possible + string[index+1:])
    return new

def only_terminals(string, cfg):
    """ Returns whether this string contains only terminals. """
    for char in string:
        if char not in cfg['terminals']:
            return False
    return True

def generate_strings(cfg, max_depth):
    """ Generates all strings up to a certain transition depth from this context free grammar. """
    level = 0
    strings = [cfg['start']]
    # While it is still generating new strings
    while level < max_depth:
        new_strings = []
        # Generate new possible strings from current strings
        for string in strings:
            new_strings += (transition(string, cfg))
        # Overwrite old states with the new states
        strings += new_strings
        # Remove duplicates
        strings = list(dict.fromkeys(strings))
        level += 1
    # print(strings)
    # Only strings that are exclusively terminals and no duplicates
    return list(filter(lambda string: only_terminals(string, cfg), strings))


def test_context_free_grammar(cfg, in_langauge):
    """ Returns True if the context free grammar produced all strings that fit in langauge. """
    global cases
    produced = generate_strings(cfg_1, 10)
    # get max length of produced strings
    max_length = len(produced[-1])
    generate_cases(cfg['terminals'], max_length)
    cases = list(filter(language, cases))
    cases = list(map(lambda case: ''.join(case), cases))
    # Sort both lists
    produced.sort()
    cases.sort()
    for i in range(len(cases)):
        if produced[i] != cases[i]:
            print(f"Failure at case: {cases[i]}")
            print(f"Context free grammar output: {produced[i]}")
            print("Terminating...")
            return False
    print(f"Context free grammar produces correct strings for all test cases up to length {max_length}!")
    return True


test_context_free_grammar(cfg_1, language)

# Optimize transitions so they all occur at once