# Let's make a calculator!
# Create recipes to populate the cookbook

cookbook = {}

class recipe:
    def __init__(self, inway, outway, stoich, time, name):
        self.inway = inway
        self.output = outway
        self.stoich = stoich
        self.time = time
        self.name = name


inway = ['copper']
outway = ['copper_cable']
stoich = {'copper':1, 'copper_cable':2}

copper_wire = recipe(inway, outway, stoich, 0.5, 'copper_wire')
cookbook.update({'copper_wire':copper_wire})

inway = ['copper_cable', 'iron_plate']
outway = ['electronic_circuit']
stoich = {'copper_cable':3, 'iron_plate':1, 'electronic_circuit':1}

electronic_circuit = recipe(inway, outway, stoich, 0.5,'electronic_circuit')
cookbook.update({'electronic_circuit':electronic_circuit})

# End cookbook

# Begin main program logic

bottleneck = ('electronic_circuit', 1)

x = cookbook.get(bottleneck[0])
print(x.inway)
# for i in x.inway:
#     print(i)
#     if i in cookbook.keys():
#         print(f'{i}in cookbook')
#     else:
#         print(f'{i} not in cookbook')

# if bottleneck[0] in cookbook:
#     print(cookbook('electronic_circuit').get(inway))
# else:
#     print('False')

