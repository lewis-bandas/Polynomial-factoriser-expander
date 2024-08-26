import re
import sys


'''
This function takes in a string of either a fraction, surd, or both, and converts
it to a float
'''
def evaluate(exact_value):
    if exact_value == "" or exact_value == "-":
        return -1 if exact_value == "-" else 1
    segments = re.split("/", exact_value)
    nums = []
    for segment in segments:
        if re.search("sqrt", segment):
            is_negative = (segment[0] == "-") 
            num = float(re.sub(".*sqrt([-0-9.]+)[^0-9.-]*", r"\1", segment))
            if num < 0:
                raise ValueError("Cannot take the square root of a negative number")
            added_num = num**0.5
            added_num = -added_num if is_negative else added_num
            nums.append(added_num)
        else:
            nums.append(float(segment))
    if len(nums) == 1:
        return nums[0]
    return nums[0] / nums[1]