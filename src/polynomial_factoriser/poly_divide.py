from collections import OrderedDict

'''this function is a modified version of the bisect.insort() method to work
with a list sorted in reverse order. It is taken from this post:
https://stackoverflow.com/questions/2247394/bisect-
is-it-possible-to-work-with-descending-sorted-lists'''
def reverse_insort(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid + 1
    a.insert(lo, x)

def long_division(poly, factor, keys):
    result = OrderedDict()
    if factor == 0:
        length = len(keys)
        for i in range(length):
            result[str(keys[i] - 1)] = poly[str(keys[i])]
    
    else:
        i = 0
        num_keys = len(keys)
        while i < num_keys - 1:
            prev = str(keys[i] - 1)
            result[prev] = poly[str(keys[i])]
            if poly.get(prev, None) is not None:
                poly[prev] -= factor * result[prev]
            else:
                poly[prev] = -(factor * result[prev])
                reverse_insort(keys, int(prev))


                num_keys += 1
                
            i += 1
            
    
    return result