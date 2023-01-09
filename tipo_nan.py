import math
from decimal import Decimal
#NaN Not a number, no es sensible a mayus / minus, es un tipo de dato numerico indefinido
a = float('NaN')
# print(f'a: {a}')
# print(f'Es NaN (not a number)?: {math.isinf(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'NaN (not a nummber)?: {math.isinf(a)}')