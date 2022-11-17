from pprint import pprint

# Let's make a calculator!
# Create recipes to populate the cookbook

# TODO
# Implement time

cookbook = {}

class recipe:
    def __init__(self, inway, outway, stoich, time):
        self.inway  = inway
        self.outway = outway
        self.stoich = stoich
        self.time   = time
        self.name   = self.outway[0]

def cooking(inway, outway, stoich, time):
    cookbook.update({outway[0]:recipe(inway,outway,stoich,time)})


inway = ['copper']
outway = ['copper_cable']
stoich = {'copper':1, 'copper_cable':2}
cooking(inway,outway,stoich,0.5)

inway = ['copper_cable', 'iron_plate']
outway = ['electronic_circuit']
stoich = {'copper_cable':3, 'iron_plate':1, 'electronic_circuit':1}
cooking(inway,outway,stoich,0.5)

inway = ['electronic_circuit', 'iron_plate']
outway = ['rail_signal']
stoich = {'electronic_circuit': 1, 'iron_plate': 5, 'rail_signal':1}
cooking(inway,outway,stoich,0.5)

inway = ['iron_plate']
outway = ['iron_gear_wheel']
stoich = {'iron_plate':2, 'iron_gear_wheel':1}
cooking(inway,outway,stoich,0.5)

inway = ['iron_gear_wheel', 'iron_plate']
outway = ['transport_belt']
stoich = {'iron_gear_wheel':1, 'iron_plate':1, 'transport_belt':2}
cooking(inway,outway,stoich,0.5)

inway = ['electronic_circuit', 'iron_gear_wheel', 'iron_plate']
outway = ['inserter']
stoich = {'electronic_circuit':5, 'iron_gear_wheel':1, 'iron_plate':1, 'inserter':1}
cooking(inway,outway,stoich,0.5)

inway = ['inserter', 'transport_belt']
outway = ['logistic_science_pack']
stoich = {'inserter':1, 'transport_belt':1, 'logistic_science_pack':1}
cooking(inway,outway,stoich,8.75)



class Node():
    def __init__(self, recipe, parent):
        self.parent     = parent
        self.child      = []
        self.recipe     = recipe
        self.mach       = None          # Inherited number of this machine for children to support
        self.name       = recipe.name
        self.time       = recipe.time

cookbook_names = list(cookbook.keys())

objs = []



############
### INIT ###
############

bottle = ('logistic_science_pack', 10)

objs.append(Node(cookbook[bottle[0]], None))
objs[0].mach = bottle[1]
root = objs[0]
current = objs[0]

x = current.recipe.inway
# print(x)
for i in current.recipe.inway:
    if i in cookbook_names:
        objs.append(Node(cookbook[i], current))
        mach_time = cookbook[i].time/current.recipe.time*current.recipe.stoich[i]/cookbook[i].stoich[i]*current.mach
        objs[-1].mach = mach_time

def child_exists(parent, child):
    '''
    Returns True if the parent has a child with child's name. False otherwise.
    '''
    for i in parent.child:
        if i.name == child:
            return True
    return False


done = False
while done == False:
    done = True
    for i in objs:
        for g in i.recipe.inway:
            if g in cookbook_names:
                if child_exists(i, g) == False:
                    objs.append(Node(cookbook[g], i))
                    i.child.append(objs[-1])
                    # i.child.append(cookbook[g])
                    done = False
        
        # Create object for child
        # for g in i.child:





# Calculate mach
for i in objs:
    if i.mach == None:
        tim = i.recipe.time/i.parent.recipe.time
        stoi = i.parent.recipe.stoich[i.recipe.name]/i.recipe.stoich[i.recipe.name]
        i.mach = tim*stoi*i.parent.mach
        # i.mach = i.recipe.time/i.parent.recipe.time*i.parent.stoich[i.recipe.name]/i.recipe.stoich[i.recipe.name]*i.parent.mach

for i in objs:
    print(f'{i.name}: {i.mach:.1f}')



