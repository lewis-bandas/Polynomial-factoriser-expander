import re
from binomial_product_expander.pascals_triangle import efficient_expand
from binomial_product_expander.binomial_multiply import brute_force_multiply
def print_as_polynomial(final_expanded_result):
    ordered_keyset = sorted(final_expanded_result.keys(), reverse=True)
    print("In expanded form, this expression can be written as", end=' ')
    for key in ordered_keyset:
        coefficient = final_expanded_result[key]
        if not (type(coefficient) is int) and coefficient.is_integer():
            coefficient = int(coefficient)
        print_coefficient = abs(coefficient) if key != ordered_keyset[0] else coefficient
        print_coefficient = "" if print_coefficient == 1 and key != 0 else print_coefficient

        if key != ordered_keyset[0]:
            print(f" {'-' if coefficient < 0 else '+'} ", end='')
        if key > 1:
            print(f"{print_coefficient}x^{key}", end='')
        elif key == 1:
            print(f"{print_coefficient}x", end='')
        elif key == 0:
            print(f"{print_coefficient}", end='')
    print()
def converted(term):
    converted_dict = {}
    converted_dict[1] = term["coefficient"]
    converted_dict[0] = term["constant"]
    return converted_dict
def make_terms_dict(terms):
    terms_dict = []
    for term in terms:
        coefficient = re.split("x", term)[0]
        if coefficient == "":
            coefficient = 1
        coefficient = int(coefficient)
        constant_term = re.sub(".*x|\^.*", "", term)
        if constant_term == "":
            constant_term = 0
        else:
            multiplier = -1 if constant_term[0] == "-" else 1
            constant_term = multiplier * int(constant_term[1:])
        power = 1 if not re.search("\^", term) else int(re.split("\^", term)[-1])
        terms_dict.append({
            "coefficient": coefficient,
            "constant": constant_term,
            "power": power
        })
    return terms_dict

def expand_product():
    product = input("Enter your binomial product in the form (ax + b)^n.\n" +
    "you can also chain multiple brackets together, (e.g (2x + 1)^2 (x - 4)).\n" + 
    "Product: ")
    product = re.sub("\s", "", product)
    terms = re.split("\(", product)
    terms = [re.sub("\(|\)", "", term) for term in terms if term != '']
    terms_dict = make_terms_dict(terms)
    expanded_terms = []
    for term in terms_dict:
        if term["power"] != 1:
            expanded_term = efficient_expand(term)
            expanded_terms.append(expanded_term)
        else:
            expanded_terms.append(converted(term))
    final_expanded_result = brute_force_multiply(expanded_terms)
    print_as_polynomial(final_expanded_result)
   