# Okay try something a little different
# Make a class for each recipe

class recipe:
    def __init__(self, recipes, input, output, time):
        self.recipes = recipes
        self.input = input
        self.output = output
        self.time = time

# Generate a few recipe objects
recipe_book = []

rrr = {
    'copper': 1,
    'copper_cable': 2,
}
inway = ['copper']
outway = ['copper_cable']
tim = 0.5
copper_cable = recipe(rrr, inway, outway, tim)
recipe_book.append(copper_cable)

rrr = {
    'copper_cable': 3,
    'iron_plate': 1,
    'electronic_circuit': 1
}
inway = ['copper_cable', 'iron_plate']
outway = ['electronic_circuit']
tim = 0.5

electronic_circuit = recipe(rrr, inway, outway, tim)
recipe_book.append(electronic_circuit)

# Test the logic

input_tracker = []

for i in electronic_circuit.input:
    input_tracker.append(i)

# print(input_tracker)

for i in input_tracker:
    if i in recipe_book:
        print(f'{i} is an intermediate')
    else:
        print(f'{i} is not an intermediate')
    
# As seen here, the calculator insists that there are no strings in the 'recipe_book' list, which contains all recipe objects.

# https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value

