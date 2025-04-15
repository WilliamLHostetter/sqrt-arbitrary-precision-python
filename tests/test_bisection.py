from sqrt_bisection import squareRootBisection

import pytest
import decimal
from decimal import Decimal
# NASA's first 1 million digits of the square root of 2 can be found at
# https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
sqrt_2_str = "1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727"


decimal.getcontext().prec = 1003
parameters_list =  [(2.0, 10, 0.0, 2.0, round(Decimal(sqrt_2_str), 10)), 
                    (2.0, 50, 0.0, 2.0, round(Decimal(sqrt_2_str), 50)), 
                    (2.0, 100, 0.0, 2.0, round(Decimal(sqrt_2_str), 100)),]
@pytest.mark.parametrize("input_number, precision_num_digits, a, b, expected", parameters_list)
def test_squareRootBisection(input_number, precision_num_digits, a, b, expected):
    '''
    Testing bisection method by comparing to NASA's calculation of sqrt(2)
    squareRootBisection(input_number: float, precision_num_digits: int, a: float, b: float) -> Decimal
    '''
    assert squareRootBisection(input_number, precision_num_digits, a, b) == expected
