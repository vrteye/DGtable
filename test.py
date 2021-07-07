import decimal

decimal.getcontext().prec = 2

a = decimal.Decimal('5.1123452')
print(a)
print(type(a))