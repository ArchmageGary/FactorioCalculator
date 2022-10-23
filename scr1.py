

# Let's make a calculator!

# Let's make a 'recipe' class

class recipe:
    def __init__(self, input, output):
        self.input = input
        self.output = output

cop_in = {
    'copper': 1,
    'time': 0.5
}

cop_out = {
    'copper_cable': 2
}

copper_wire = recipe(cop_in, cop_out)
print(copper_wire.input)

circ_in = {
    'time': 0.5,
    'copper_cable': 3,
    'iron_plate': 1
}

circ_out = {
    'electronic circuit': 1
}

electronic_circuit = recipe(circ_in, circ_out)

