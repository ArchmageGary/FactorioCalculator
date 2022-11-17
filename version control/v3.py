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
        self.layer      = 0
        if self.parent != None:
            self.layer = self.parent.layer +1

cookbook_names = list(cookbook.keys())

############
### INIT ###
############

bottle = ('logistic_science_pack', 10)

objs = []
objs.append(Node(cookbook[bottle[0]], None))
objs[0].mach = bottle[1]
root = objs[0]
current = objs[0]

# Single loop that will generate the whole tree, parent/child relationships and machine ratio
done = False
next = [root]
while done == False:
    n = 0
    done = True
    for i in next:
        if n == 0:
            next = []
        for g in i.recipe.inway:
            if g in cookbook_names:
                objs.append(Node(cookbook[g], i))
                next.append(objs[-1])
                # Set machine count 'mach'
                node = objs[-1]
                if node.mach == None:
                    tim = node.recipe.time / node.parent.recipe.time
                    stoi = node.parent.recipe.stoich[node.recipe.name] / node.recipe.stoich[node.recipe.name]
                    node.mach = tim*stoi*node.parent.mach
                    
                done = False
            n += 1

for i in objs:
    if i == root:
        print(f'{i.mach} machines making {i.name}: root')
        continue
    print(f'{i.mach:.1f} machines generating {i.name}{(20-len(i.name))*" "} for {i.parent.name}{" "*(25-len(i.parent.name))}: layer {i.layer}')

