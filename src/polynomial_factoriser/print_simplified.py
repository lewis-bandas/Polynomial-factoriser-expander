
from collections import OrderedDict

def print_non_factorised(roots, terms, keys):
    num_roots = len(roots)
    if num_roots > 0:
        print("(", end = "")
    length = len(keys)
    for i in range(length):
        if i == 0:
            print(f"x^{str(keys[i])}", end = " ")
        else:
            if terms[str(keys[i])] < 0:
                print("-", end = " ")
            elif terms[str(keys[i])] > 0:
                print("+", end = " ")
            else:
                continue
            to_print = abs(terms[str(keys[i])])
            if to_print == 1 and str(keys[i]) != "0":
                to_print = ""
            if str(keys[i]) == "1":
                print(f"{str(to_print)}x", end = "")
            elif str(keys[i]) == "0":
                print(f"{str(to_print)}", end = "")
            else:
                print(f"{str(to_print)}x^{str(keys[i])}", end = "")
            if i != length - 1:
                print(" ", end = "")
    if num_roots > 0:
        print(")", end = "")
    print(".")


def print_factorised(roots):
    num_roots = len(roots)
    roots_dict = OrderedDict()
    for i in range(num_roots):
        roots_dict[str(roots[i])] = roots.count(roots[i])

    for key in roots_dict:
        root = int(key)
        to_print = str(abs(root))
        power = roots_dict[key]
        if root < 0:
            if power == 1:
                print(f"(x - {to_print})", end = " ")
            else:
                print(f"(x - {to_print})^{str(power)}", end = " ")
        elif root > 0:
            if power == 1:
                print(f"(x + {to_print})", end = " ")
            else:
                print(f"(x + {to_print})^{str(power)}", end = " ")
        else:
            if power == 1:
                print(f"x", end = " ") 
            else:
                print(f"x^{str(power)}", end = " ") 