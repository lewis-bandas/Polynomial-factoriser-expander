from collections import defaultdict
def expression_multiply(term, combined):
    result = defaultdict(int)
    for power in term.keys():
        for other_power in combined.keys():
            multiplicity = power + other_power
            result[multiplicity] += term[power] * combined[other_power]
    return result


def brute_force_multiply(terms):
    if len(terms) == 1:
        combined = terms[0]
        return combined
    combined = brute_force_multiply(terms[1:])
    term = terms[0]
    return expression_multiply(term, combined)