def calculate(units):
    if units<=100:return units*3
    if units<=300:return 300+(units-100)*5
    return 1300+(units-300)*8
