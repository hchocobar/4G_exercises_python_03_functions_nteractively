def dollar_to_euro(dollar_value):
	return dollar_value * 0.89


def euro_to_yen(euro_value):
	return euro_value * 124.15


# Your code below
print(euro_to_yen(dollar_to_euro(137)))  # Salida: 15137.609500000002
