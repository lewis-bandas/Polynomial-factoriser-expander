import sys
import math


def is_same_angle(a1, a2):
    a1 = abs(a1)
    a2 = abs(a2)
    og = min(a1, a2)
    bigger = max(a1, a2)
    return bigger == 180 - og or bigger == 360 - og or bigger == og
    

'''find the auxiliary angle if the expression was expressed as Rsin(x + a)'''
def find_auxiliary_sine(coefficients, r, silent_mode, round_to):
    a1 = round(math.degrees(math.acos(coefficients["sin"] / r)), round_to)
    a2 = round(math.degrees(math.asin(coefficients["cos"] / r)), round_to)
    same_angle = is_same_angle(a1, a2)
    if a1 != a2 and not same_angle:
        silent_mode or print("This expression cannot be expressed in the form Rsin(x + a) or Rcos(x + a)")
        sys.exit()
    a = min([a1, a2])
    if a1 < 0 or a2 < 0:
        temp_a1 = abs(a1)
        temp_a2 = abs(a2)
        temp = min(temp_a1, temp_a2)
        a = (a1 if temp == temp_a1 else a2)
    if same_angle and a1 != a2:
        if a == a1:
            a = round(360.0, round_to) - a
        else:
           a = round(180.0, round_to) - a
    return a