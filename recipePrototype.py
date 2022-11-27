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

