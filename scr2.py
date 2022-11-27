from pprint import pprint
from igraph import *

# Let's make a calculator!
# Create recipes to populate the cookbook

# TODO
# Implement time

# Trying to make a cookbook template that is easier for those inputting recipes
# while still working with existing tree logic.
# The goal is to export a cookbook that will still work in the main program.

cookbook = {}

class recipe:
    def __init__(self, name, inway, outway, stoich, time):
        self.name   = name              # String to act as primary output name
        self.inway  = inway             # List of inpus
        self.outway = outway            # List of output
        self.stoich = stoich            # Stoichiometry ratios of all inputs and outputs
        self.time   = time              # Base recipe time

class recipe2:
    def __init__(self, name, inbound, outbound, time):
        self.name   = name
        self.inway  = list(inbound.keys())
        self.outway = list(outbound.keys())
        self.stoich = inbound | outbound
        self.time   = time


def cooking(name, inway, outway, stoich, time):
    cookbook.update({outway[0]:recipe(name, inway,outway,stoich,time)})

def cooking2(name, inbound, outbound, time):
    cookbook.update({name:recipe2(name, inbound, outbound, time)})




# This is the recipe1 template for recipes
name        = 'copper cable'                            # String with name of primary output
inway       = ['copper']                                # List of all inputs
outway      = ['copper cable']                          # List of all outputs
stoich      = {'copper':1, 'copper cable':2}            # Dict will all ratios in recipe
timmy       = 0.5                                       # Base recipe time
cooking(name,inway,outway,stoich,timmy)

# This is the recipe2 template for recipes
name        = 'electronic circuit'
inbound     = {'copper cable':3, 'iron plate':1}
outbound    = {'electronic circuit':1}
timmy       = 0.5
cooking2    (name, inbound, outbound, timmy)




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
            self.layer  = self.parent.layer +1
        self.id         = len(objs)
        self.color      = 'green'

cookbook_names = list(cookbook.keys())

############
### INIT ###
############

bottle = ('electronic circuit', 10)

objs = []
objs.append(Node(cookbook[bottle[0]], None))
objs[0].mach = bottle[1]
root = objs[0]
root.color = 'red'
current = objs[0]
edgelist = []
namelist = []

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
                edgelist.append((objs[-1].parent.id, objs[-1].id))
                # namelist.append((objs[-1].parent.id, objs[-1].id))
                    
                done = False
            n += 1

for i in objs:
    if i == root:
        print(f'{i.mach} machines making {i.name}: root')
        continue
    print(f'{i.mach:.1f} machines generating {i.name}{(20-len(i.name))*" "}| for {i.parent.name}{" "*(25-len(i.parent.name))} | layer {i.layer} | ID:{i.id}')

# edgelist is a list of tuples linking the tree together
print(edgelist)

# namelist is a list of names, associated with id.
namelist  = []
colorlist = []
orderlist = []
layerlist = []
for i in objs:
    namelist.append(i.name + ': ' + str(f'{i.mach:.1f}'))
    colorlist.append(i.color)
    orderlist.append(i.layer)
    layerlist.append('l' + str(i.layer))


g = Graph(edgelist, directed=True)
# Add ids and labels to vertices
for i in range(len(g.vs)):
    g.vs[i]["id"]= i
    g.vs[i]["label"]= namelist[i]
    g.vs[i]['weight'] = None
g.add_edges(edgelist)


# Begin defining graph characteristics
visual_style = {}
out_name = "graph.png"
visual_style['label'] = namelist
visual_style['color'] = colorlist

# Set bbox and margin
# Future development: Auto-scale margin to be half the widest label
# Auto-scale size to fit number of nodes? Or levels? Both?
# Could count the width of widest layer and use that for w
visual_style["bbox"] = (1920,1080)
visual_style["margin"] = 140

# Set vertex colours
visual_style["vertex_color"] = 'white'
visual_style["vertex_size"] = 45
visual_style["vertex_label_size"] = 22

# Don't curve the edges
visual_style["edge_curved"] = False

# Set the layout
my_layout = g.layout_sugiyama()
visual_style["layout"] = my_layout

# Plot the graph
plot(g, out_name, **visual_style)