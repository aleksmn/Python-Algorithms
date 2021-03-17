# This based on this tutorial
# https://www.python-course.eu/polynomial_class_in_python.php

def p(x):
    return x**4 - 4*x**2 + 3*x

for x in [-1, 0, 2, 3.4]:
    print(x, p(x))

