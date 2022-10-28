# Let's make a calculator!
# Create recipes to populate the cookbook

# TODO
# Implement time

cookbook = {}

class recipe:
    def __init__(self, inway, outway, stoich, time):
        self.inway = inway
        self.outway = outway
        self.stoich = stoich
        self.time = time


inway = ['copper']
outway = ['copper_cable']
stoich = {'copper':1, 'copper_cable':2}

copper_cable = recipe(inway, outway, stoich, 0.5)
cookbook.update({'copper_cable':copper_cable})

inway = ['copper_cable', 'iron_plate']
outway = ['electronic_circuit']
stoich = {'copper_cable':3, 'iron_plate':1, 'electronic_circuit':1}

electronic_circuit = recipe(inway, outway, stoich, 0.5)
cookbook.update({'electronic_circuit':electronic_circuit})

inway = ['electronic_circuit', 'iron_plate']
outway = ['rail_signal']
stoich = {'electronic_circuit': 1, 'iron_plate': 5, 'rail_signal':1}

rail_signal = recipe(inway, outway, stoich, 0.5)
cookbook.update({'rail_signal':rail_signal})

inway = ['iron_plate']
outway = ['iron_gear_wheel']
stoich = {'iron_plate':2, 'iron_gear_wheel':1}

iron_gear_wheel = recipe(inway, outway, stoich, 0.5)
cookbook.update({'iron_gear_wheel':iron_gear_wheel})

inway = ['iron_gear_wheel', 'iron_plate']
outway = ['transport_belt']
stoich = {'iron_gear_wheel':1, 'iron_plate':1, 'transport_belt':2}

transport_belt = recipe(inway,outway,stoich,0.5)
cookbook.update({'transport_belt':transport_belt})

inway = ['electronic_circuit', 'iron_gear_wheel', 'iron_plate']
outway = ['inserter']
stoich = {'electronic_circuit':5, 'iron_gear_wheel':1, 'iron_plate':1, 'inserter':1}

inserter = recipe(inway,outway,stoich,0.5)
cookbook.update({'inserter':inserter})

inway = ['inserter', 'transport_belt']
outway = ['logistic_science_pack']
stoich = {'inserter':1, 'transport_belt':1, 'logistic_science_pack':1}

logistic_science_pack = recipe(inway, outway, stoich, 8.75)
cookbook.update({'logistic_science_pack':logistic_science_pack})




# End cookbook

# Begin main program logic

def get_intermediates(name, machine_count):
    '''
    Given the name of a recipe object, returns intermediates
    '''
    new_list = []
    for i in cookbook[name].inway:
        if i in cookbook_names:
            new_list.append((name,i, machine_count))
    if new_list == []:
        return None
    else:
        return new_list

def main_func(name, material, machine_count):
    '''
    Given current goal recipe name, material in question and machine count,
    will print ratio instructions and update this_batch.
    '''
    inward = cookbook.get(name).stoich[material]
    outward = cookbook.get(material).stoich[material]
    time_ratio = cookbook.get(material).time/cookbook.get(name).time
    mach_count = inward/outward*machine_count*time_ratio
    print(f'{mach_count:.1f}{" "*(5-len(str(mach_count)))} machines producing {material}{" "*(25-len(str(material)))} per this size batch of {name}')
    new_list = []
    for i in cookbook[material].inway:
        if i in cookbook_names:
            new_list.append((material,i, mach_count))
    return new_list

# Bottle needs a string recipe title and machine count
bottle = ('logistic_science_pack', 10)
cookbook_names = list(cookbook.keys())

layer = 1
this_batch = get_intermediates(bottle[0], bottle[1])

while this_batch != []:
    print(f'Begin layer {layer} ####')
    n=1
    for i in this_batch:
        if n == 1: this_batch = []
        this_batch += main_func(i[0],i[1],i[2])
        n+=1
    layer += 1
