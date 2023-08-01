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
            num = float(re.sub(".*sqrt([-0-9.]+)[^0-9.-]*", r"\1", segment))
            if num < 0:
                raise ValueError("Cannot take the square root of a negative number")
            nums.append(num**0.5)
        else:
            nums.append(float(segment))
    if len(nums) == 1:
        return nums[0]
    return nums[0] / nums[1]