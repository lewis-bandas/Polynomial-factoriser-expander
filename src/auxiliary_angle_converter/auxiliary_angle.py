import sys
import re
from auxiliary_angle_converter.exact_value_convert import evaluate
from auxiliary_angle_converter.find_auxiliary import find_auxiliary_sine

def auxiliary_angle_convert():
    expression = input("Enter the expression in the form Asinx +/- Bcosx (order does not matter).\n" + 
    "You can use round brackets anywhere to make the expression look cleaner, but it is not necessary.\n" +
    "You can also enter fractions in the form a/b (where a and b are not fractions),\n" + 
    "as well as surds in the form sqrt(n), where n is a whole number.\n" +
    "Expression: ")
    expression = re.sub("[()]", "", expression)
    if not re.search(" +[+-] +", expression):
        print(f"This is already fully simplified, as {expression}")
        sys.exit()
    operation = re.search(" +[+-] +", expression).group()
    operation = re.sub("\s+", "", operation)
    terms = re.split(f" +\\{operation} +", expression)
    terms = [re.sub("\s+", "", term) for term in terms if term != '']
    coefficients = {
        "cos": [evaluate(re.sub("(.*)(cosx)", r"\1", term)) for term in terms \
            if re.search("cosx", term)][0],
        "sin": [evaluate(re.sub("(.*)(sinx)", r"\1", term)) for term in terms \
            if re.search("sinx", term)][0]
    }
    if (coefficients["cos"] == 0 or coefficients["sin"] == 0):
        to_print = re.sub('0(sinx|cosx)', '', expression)
        to_print = re.sub(".*([0-9]*(sinx|cosx)).*", r"\1", to_print)
        print(f"This is already fully simplified, as {to_print}")
        sys.exit()
    if operation == "-":
        index = re.search("cos|sin", terms[1]).group()
        coefficients[index] = -coefficients[index]
    r = (surd_value := round(coefficients["sin"]**2 + coefficients["cos"]**2, 5))**0.5
    if not type(surd_value) is int and surd_value.is_integer():
        surd_value = int(surd_value)
    a_sine = find_auxiliary_sine(coefficients, r)
    if a_sine - 180.0 > 0.0:
        a_sine -= 360.0
        a_sine = round(a_sine, 2)
    '''if we have sin(x + a), the cos equivalent is cos(90 - a - x), and since in 
    this expression we have "-x", it's not in the form cos(x + a). To remedy this,
    we can use the rule that cos(-x) = cos(x), giving us cos(x + a - 90).'''
    a_cosine = -(90.0 - a_sine)
    print_r = str(int(r)) if r.is_integer() else f"sqrt({surd_value})"
    print_r = "" if r == 1 else print_r
    cos_symbol = "+" if a_cosine >= 0 else "-"
    sin_symbol = "+" if a_sine >= 0 else "-"
    print(f"This expression can be written in the form {print_r}sin(x {sin_symbol} {abs(a_sine)}°),\n" + 
    f"as well as {print_r}cos(x {cos_symbol} {abs(a_cosine)}°) (to 2 d.p). These are only some of many solutions.")
    
    
