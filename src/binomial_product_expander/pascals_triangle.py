from math import factorial

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))
    
def efficient_expand(product):
    expanded = {}
    n = product["power"]
    a = product["coefficient"]
    b = product["constant"]
    for i in range(n + 1):
        num = n - i
        expanded[num] = combination(n, i) * (a**num) * (b**i)
    return expanded