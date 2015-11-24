#!/usr/bin/python3

from collections import Counter

# Expected value
def expected_value(lst):
    c = Counter(lst)
    n = len(lst)
    
    return sum(
    	map(
    		lambda t: t[0] * (t[1] / n), 
    		zip(c.keys(),c.values())
    	)
    )
