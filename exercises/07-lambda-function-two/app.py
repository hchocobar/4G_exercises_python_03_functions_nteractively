""" 
PEP8 E731 do not assign a lambda expression, use a def
rapid = lambda n: n % 2 == 1  # Esto funciona, pero es incorrecto
"""

# Las cadenas son iterables, por ello utilizo slice o rodajas
def rapid(line):
    return line[:-1]


# From this line above, plese do not change code below
print(rapid("bob"))  # Salida: bo
print(rapid('líneas'))  # Salida: línea
