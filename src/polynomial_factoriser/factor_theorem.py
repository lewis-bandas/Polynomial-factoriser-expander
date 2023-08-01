
'''this function checks for both negative and positive just to save the time of 
calling the function twice'''
def check_if_root(terms, num):
    func_value = 0
    for key in terms:
        func_value += terms[key] * (num**(int(key)))
    if (func_value == 0):
        return num
    num = -num
    func_value = 0
    for key in terms:
        func_value += terms[key] * (num**(int(key)))
    if (func_value == 0):
        return num
    return None

def factor_theorem(terms):
    if terms.get("0", None) is not None:
        constant = terms["0"]
    else:
        constant = 0
        return constant
    highest_factor = abs(constant)**0.5
    root = None
    for i in range(1, int(highest_factor) + 1):
        if constant % i == 0:
            root = check_if_root(terms, i)
            if root != None:
                return root
    return None

