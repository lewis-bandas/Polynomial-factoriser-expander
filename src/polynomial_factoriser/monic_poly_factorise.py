from polynomial_factoriser.poly_setup import setup_terms
from polynomial_factoriser.factor_theorem import factor_theorem
import sys
from collections import OrderedDict
from polynomial_factoriser.poly_divide import long_division
from polynomial_factoriser.print_simplified import print_factorised, print_non_factorised

def poly_factorise():
    polynomial = input("Enter your polynomial (in the form x^n +/- bx^n-1 +/- ... +/- cx +/- d).\n" \
    + "If you put in fractions or random nonsense characters there is a very high\n" + \
    "chance this program will crash, " + "so dont try to be mr funny man. This program\n" + \
    "also will not find complex roots (at least not intentionally). Order of terms does not matter.\n" +\
    "Anyway, enter the thing: ")
    terms = OrderedDict()
    words = polynomial.split()
    terms = setup_terms(terms, words)
    keys = sorted([int(key) for key in terms.keys()], reverse=True)
    if keys[0] < 2 or len(terms) < 2:
        print("")
        print("This either cannot be factorised or is incredibly simple.\n" + \
        "Come on now.")
        sys.exit()
    num_keys = len(keys)
    j = 0
    while j < num_keys:
        if terms[str(keys[j])] == 0:
            terms.pop(str(keys[j]), None)
            keys.remove(keys[j])
            num_keys -= 1
        else:
            j += 1
    if terms[str(keys[0])] != 1:
        print("")
        print("This program only works for monic polynomials. Try using\n" + \
        "something not designed by a complete amateur next time.")
        sys.exit()
    roots = []
    while keys[0] >= 2:
        factor = factor_theorem(terms)
        if factor is None:
            print("")
            print("This polynomial either cannot be fully factorised, contains complex\n" + \
            "roots, or both. With all its integer roots, it can be written as", end = " ")
            print_factorised(roots)
            print_non_factorised(roots, terms, keys)
            sys.exit()
        factor = -int(factor)
        roots.append(factor)
        terms = long_division(terms, factor, keys)
        
        keys = sorted([int(key) for key in terms.keys()], reverse=True)
        
    roots.append(terms.get("0", 0))
    print("")
    print("This polynomial can be fully factorised to ", end = "")
    print_factorised(roots)
    print("\b.")

        