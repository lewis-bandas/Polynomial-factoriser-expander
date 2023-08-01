import sys
from polynomial_factoriser.monic_poly_factorise import poly_factorise
from auxiliary_angle_converter.auxiliary_angle import auxiliary_angle_convert
from binomial_product_expander.binomial_product import expand_product


if len(sys.argv) <= 1:
    print(f"usage: {sys.argv[0]} <mode>")
    print("Mode 1: factorise any monic polynomial")
    print("Mode 2: convert a sum of a sine term and a cosine term to the form\n" +
    "Rsin(x + a) or Rcos(x + a), where \"a\" is an angle in degrees")
    print("Mode 3: expand a binomial product into a polynomial")
    sys.exit()
mode = int(sys.argv[1])
if mode == 1:
    poly_factorise()
elif mode == 2:
    auxiliary_angle_convert()
elif mode == 3:
    expand_product()
else:
    print("Invalid mode")
    


