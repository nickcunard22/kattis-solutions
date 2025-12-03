'''
maintain what the most usd or cad we could have at any given day is
then at each day, check if converting would give us more
update max if so
'''
import math

def cad_to_usd(balance, rate):
    balance /= rate
    balance -= balance * .03
    balance *= 100
    balance = math.floor(balance)
    balance /= 100
    return balance

def usd_to_cad(balance, rate):
    balance *= rate
    balance -= balance * .03
    balance *= 100
    balance = math.floor(balance)
    balance /= 100
    return balance


while cases := int(input()):
    rates = [float(input()) for _ in range(cases)]
    
    max_cad = 1000
    max_usd = -1
    for rate in rates:
        max_usd = max(cad_to_usd(max_cad, rate), max_usd)
        max_cad = max(usd_to_cad(max_usd, rate), max_cad)

    print(f"{max_cad:.2f}")
