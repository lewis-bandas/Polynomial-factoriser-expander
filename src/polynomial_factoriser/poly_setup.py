import sys
import re
def get_multiple(words, sign, i):
    word = words[i]
    num = re.split("x", word)[0]
    if num == "" or num == "-":
        to_return = 1 if num == "" else -1
        to_return = -to_return if sign[i] == "-" else to_return
        return to_return
    num = int(num)
    if sign[i] == "-":
        num = -num
    return num
def setup_terms(terms, words):
    num_words = len(words)
    sign = ['+' for _ in range(num_words)]
    for i in range(num_words):
        if ('(' in words[i] or ')' in words[i]):
            print("")
            print("You've used brackets, meaning either the polynomial is\n" + \
            "already factorised, or you're being mr funny man. Next.")
            sys.exit()

        if (words[i] == "+" or words[i] == '-'):
            sign[i + 1] = words[i][0]
            continue
        length_word = len(words[i])
        if '^' not in words[i]:
            multiple = 0
            power = None
            if (words[i][-1] == 'x'):
            
                multiple = get_multiple(words, sign, i)
                power = "1"
            else:
                multiple = int(words[i])
                if sign[i] == '-':
                    multiple = -multiple
                power = "0"
            if terms.get(power, None) is None:
                terms[power] = multiple
            else:
                terms[power] += multiple
        else:
            j = 0
            for j in range(length_word):
                if words[i][j] == '^':
                    j += 1
                    break
            power = ""
            while j < length_word:
                power += words[i][j]
                j += 1
            multiple = get_multiple(words, sign, i)
            if int(power) < 0:
                print("")
                print("Negative powers? Seriously?? You have severely overestimated " + \
                "my abilities.")
                sys.exit()
            if terms.get(power, None) is None:
                terms[power] = multiple
            else:
                terms[power] += multiple
    return terms
