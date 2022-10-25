# Let's make a calculator!
# Create recipes to populate the cookbook

cookbook = {}

class recipe:
    def __init__(self, inway, outway, stoich, time, name):
        self.inway = inway
        self.outway = outway
        self.stoich = stoich
        self.time = time
        self.name = name


inway = ['copper']
outway = ['copper_cable']
stoich = {'copper':1, 'copper_cable':2}

copper_cable = recipe(inway, outway, stoich, 0.5, 'copper_cable')
cookbook.update({'copper_cable':copper_cable})

inway = ['copper_cable', 'iron_plate']
outway = ['electronic_circuit']
stoich = {'copper_cable':3, 'iron_plate':1, 'electronic_circuit':1}

electronic_circuit = recipe(inway, outway, stoich, 0.5,'electronic_circuit')
cookbook.update({'electronic_circuit':electronic_circuit})

# End cookbook

# Begin main program logic

bottleneck = cookbook.get('electronic_circuit')

x = cookbook.get(bottleneck.name)
cookbook_names = list(cookbook.keys())
print(cookbook_names)
# print(x.inway)


# Goal: output '1.5 machinges outputting "copper_cable" needed'
intermediate = []

for i in cookbook.get(bottleneck.name).inway:
    print(i)
    if i in cookbook_names:
        print(f'{i} is an intermediate')
        push = 
        intermediate.append(i)

    else:
        print(f'{i} is not an intermediate')

for i in intermediate:
    x = cookbook.get(i).stoich[i]
    print(x)