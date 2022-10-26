# Let's make a calculator!
# Create recipes to populate the cookbook

# TODO
# Implement time
# Implement multi-ingredient layering

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

inway = ['iron_plate']
outway = ['iron_gear_wheel']
stoich = {'iron_plate':2, 'iron_gear_wheel':1}

iron_gear_wheel = recipe(inway, outway, stoich, 0.5, 'iron_gear_wheel')
cookbook.update({'iron_gear_wheel':iron_gear_wheel})

inway = ['iron_gear_wheel', 'iron_plate']
outway = ['transport_belt']
stoich = {'iron_gear_wheel':1, 'iron_plate':1, 'transport_belt':2}

transport_belt = recipe(inway,outway,stoich,0.5,'transport_belt')
cookbook.update({'transport_belt':transport_belt})

inway = ['electronic_circuit', 'iron_gear_wheel', 'iron_plate']
outway = ['inserter']
stoich = {'electronic_circuit':1, 'iron_gear_wheel':1, 'iron_plate':1, 'inserter':1}

inserter = recipe(inway,outway,stoich,0.5,'transport_belt')
cookbook.update({'inserter':inserter})


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
    print(f'{inward/outward} machines producing {material} per this size batch of {name}')

def get_intermediates(name):
    '''
    Given the name of a recipe object, returns intermediates
    '''
    new_list = []
    for i in cookbook[name].inway:
        if i in cookbook_names:
            new_list.append((name,i))
    if new_list == []:
        return None
    else:
        return new_list

bottle = 'inserter'
cookbook_names = list(cookbook.keys())

layer = 1
this_batch = [get_intermediates(bottle)]

while this_batch != []:
    print(f'Begin layer {layer} ####')
    # print(this_batch)
    n=1
    for i in this_batch:
        if n == 1: this_batch = []
        # print(f'Layer {layer}, {i}')
        get_stoich(i[0][0],i[0][1])
        if get_intermediates(i[0][1]) != None:
            this_batch.append(get_intermediates(i[0][1]))
        n+=1
    layer += 1
    # print(f'next_batch = {this_batch}')
