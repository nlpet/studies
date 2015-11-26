#!/usr/bin/python3

from collections import Counter

# Mean value
def mean_value(lst):
    c = Counter(lst)
    n = len(lst)
    
    return sum(
    	map(
    		lambda t: t[0] * (t[1] / n), 
    		zip(c.keys(),c.values())
    	)
    )

def expected_value(lst, probs):
    prod = lambda t : t[0] * t[1]
    return sum(map(prod, zip(lst, probs)))


if __name__ == '__main__':
    ev = expected_value(range(1,7),[1/6]*6)
    print("Expected value of a 4-sided die is {}".format(ev))
