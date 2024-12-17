
import math
from fractions import Fraction

def parse_operand(operand, value):
    if value == 0.0:
        return ""
    else:
        return f" {operand} {value}"

def parse_numerator(coefficient):
    # coefficient should not be zero
    if coefficient == 1:
        return ""
    return str(coefficient)
    
def degrees_to_radians(angle, round_to):
    angle = float(angle)
    if angle == 0.0:
        return angle # so that later call of parse_operand function returns an empty string
    if angle.is_integer() and not round_to == 0:
        angle = int(angle)
        fraction = Fraction(angle, 180)
        numerator = fraction.numerator
        denominator = fraction.denominator
        if denominator == 1:
            return f"{parse_numerator(numerator)}\\pi"
        return "\\frac{" + parse_numerator(numerator) + "\\pi}{" + str(denominator) + "}"
    else:
        retval = round(angle * (math.pi / 180.0), round_to)
        if round_to == 0:
            return int(retval)
        return retval
        