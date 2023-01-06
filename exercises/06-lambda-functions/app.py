""" 
PEP8 E731 do not assign a lambda expression, use a def
is_odd = lambda n: n % 2 == 1  # Esto funciona, pero es incorrecto
"""
def is_odd(n):
    return n % 2 == 1


print(is_odd(3))
