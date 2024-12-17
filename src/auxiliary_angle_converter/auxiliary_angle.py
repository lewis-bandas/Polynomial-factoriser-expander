import sys
import re
from auxiliary_angle_converter.exact_value_convert import evaluate
from auxiliary_angle_converter.find_auxiliary import find_auxiliary_sine
from auxiliary_angle_converter.angle_convert import degrees_to_radians, parse_operand

def auxiliary_angle_convert():
    expression = input("Enter the expression in the form Asinx +/- Bcosx (order does not matter).\n" + 
    "You can use round brackets anywhere to make the expression look cleaner, but it is not necessary.\n" +
    "You can also enter fractions in the form a/b (where a and b are not fractions),\n" + 
    "as well as surds in the form sqrt(n), where n is a whole number.\n" +
    "Expression: ")
    auxiliary_angle_compute(expression, False, 5, False)
    
    
def auxiliary_angle_compute(expression, silent_mode, round_to, format_radians):
    already_simplified = False
    expression = re.sub("[()]", "", expression)
    if not re.search(" +[+-] +", expression):
        silent_mode or print(f"This is already fully simplified, as {expression}")
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
        already_simplified = True
        to_print = re.sub('0(sinx|cosx)', '', expression)
        to_print = re.sub(".*([0-9]*(sinx|cosx)).*", r"\1", to_print)
        if coefficients["cos"] == 0 and coefficients["sin"] == 0:
            to_print = "0"
        silent_mode or print(f"This is already fully simplified, as {to_print}")
        if not silent_mode:
            sys.exit()
        if to_print == "0":
            return {"sin": "0", "cos": "0", "already_simplified": already_simplified}
        
    if operation == "-":
        index = re.search("cos|sin", terms[1]).group()
        coefficients[index] = -coefficients[index]
    r = (surd_value := coefficients["sin"]**2 + coefficients["cos"]**2)**0.5
    surd_value = round(surd_value, round_to)
    if not type(surd_value) is int and surd_value.is_integer():
        surd_value = int(surd_value)
    a_sine = find_auxiliary_sine(coefficients, r, silent_mode, round_to)
    if abs(a_sine) - 180.0 > 0.0:
        if a_sine > 0:
            a_sine -= round(360.0, round_to)
        else:
            a_sine += round(360.0, round_to)
        a_sine = round(a_sine, round_to)
    '''if we have sin(x + a), the cos equivalent is cos(90 - a - x), and since in 
    this expression we have "-x", it's not in the form cos(x + a). To remedy this,
    we can use the rule that cos(-x) = cos(x), giving us cos(x + a - 90).'''
    a_cosine = round(-(90.0 - a_sine), round_to)
    int_r = round(r, round_to)
    print_r = str(int(int_r)) if int_r.is_integer() else f"sqrt({surd_value})"
    print_r = "" if r == 1 else print_r
    cos_symbol = "+" if a_cosine >= 0 else "-"
    sin_symbol = "+" if a_sine >= 0 else "-"
    a_sine = abs(a_sine)
    a_cosine = abs(a_cosine)
    silent_mode or print(f"This expression can be written in the form {print_r}sin(x{parse_operand(sin_symbol, a_sine)}°),\n" + 
    f"as well as {print_r}cos(x{parse_operand(cos_symbol, a_cosine)}°) (to 2 d.p). These are only some of many solutions.")
    if not int_r.is_integer():
        print_r = "\\sqrt{" + str(surd_value) + "}"
    if a_sine.is_integer():
        a_sine = int(a_sine)
    if a_cosine.is_integer():
        a_cosine = int(a_cosine)
    if format_radians == "true":
        a_sine = degrees_to_radians(a_sine, round_to)
        a_cosine = degrees_to_radians(a_cosine, round_to)
        return {"sin": f"{print_r}\\sin(x{parse_operand(sin_symbol, a_sine)})",
            "cos": f"{print_r}\\cos(x{parse_operand(cos_symbol, a_cosine)})",
            "already_simplified": already_simplified}
    return {"sin": f"{print_r}\\sin(x{parse_operand(sin_symbol, a_sine)}°)",
            "cos": f"{print_r}\\cos(x{parse_operand(cos_symbol, a_cosine)}°)",
            "already_simplified": already_simplified}