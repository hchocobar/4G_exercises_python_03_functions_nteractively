# Your code goes here:
def render_person(name, birthdate, color_eyes, age, genere):
    leyend = name + ' is a ' + str(age) + ' years old ' + genere + ' born in ' + birthdate + ' with ' + color_eyes + ' eyes'
    return leyend


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
