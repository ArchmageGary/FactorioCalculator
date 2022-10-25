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

inway = ['electronic_circuit', 'iron_plate']
outway = ['rail_signal']
stoich = {'electronic_circuit': 1, 'iron_plate': 5, 'rail_signal':1}

rail_signal = recipe(inway, outway, stoich, 0.5, 'rail_signal')
cookbook.update({'rail_signal':rail_signal})

# End cookbook

# Begin main program logic

def get_stoich(name, material):
    '''
    Given the name of a recipe object to provide for
    and the material name in question,
    will return that material's machine ratio.
    '''
    inward = cookbook.get(name).stoich[material]
    outward = cookbook.get(material).stoich[material]
    print(f'{inward/outward} machines producing {material} per batch of {name}')

def get_intermediates(name):
    '''
    Given the name of a recipe object, returns intermediates
    '''
    new_list = []
    for i in cookbook[name].inway:
        if i in cookbook_names:
            new_list.append((name,i))
    return new_list

bottle = 'electronic_circuit'
cookbook_names = list(cookbook.keys())

layer = 1
next_batch = []
this_batch =get_intermediates(bottle)
print(this_batch)

for i in this_batch:
    get_stoich(i[0],i[1])