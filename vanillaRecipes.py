# This is where vanilla recipes will be saved. Let's get to work!
# I will now seperate out name from outway. This will do two things: Make it scale more effectively if I make a parser,
# and give a sort of "title" at the top of the recipe to identify what it is.

cookbook = {}

class recipe:
    def __init__(self, name, inway, outway, stoich, time):
        self.name   = name              # String to act as primary output name
        self.inway  = inway             # List of inpus
        self.outway = outway            # List of output
        self.stoich = stoich            # Stoichiometry ratios of all inputs and outputs
        self.time   = time              # Base recipe time

def cooking(name, inway, outway, stoich, time):
    cookbook.update({outway[0]:recipe(name, inway,outway,stoich,time)})




# This is the current template for recipes
name        = 'copper cable'                            # String with name of primary output
inway       = ['copper']                                # List of all inputs
outway      = ['copper cable']                          # List of all outputs
stoich      = {'copper':1, 'copper cable':2}            # Dict will all ratios in recipe
timmy       = 0.5                                       # Base recipe time
cooking(name,inway,outway,stoich,timmy)


#############################
### Intermediate Products ###
#############################

# Basic?
name        = 'copper cable'
inway       = ['copper']
outway      = ['copper cable']
stoich      = {'copper':1, 'copper cable':2}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'iron stick'
inway       = ['iron plate']
outway      = ['iron stick']
stoich      = {'iron plate':1, 'iron stick':2}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'iron gear wheel'
inway       = ['iron plate']
outway      = ['iron gear wheel']
stoich      = {'iron plate':2, 'iron gear wheel':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'empty barrel'
inway       = ['steel plate']
outway      = ['empty barrel']
stoich      = {'steel plate':1, 'empty barrel':1}
timmy       = 1
cooking(name,inway,outway,stoich,timmy)


# Circuits
name        = 'electronic circuit'
inway       = ['copper cable', 'iron plate']
outway      = ['electronic circuit']
stoich      = {'copper cable':3, 'iron plate':1, 'electronic circuit':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'advanced circuit'
inway       = ['copper cable', 'electronic circuit', 'plastic bar']
outway      = ['advanced circuit']
stoich      = {'copper cable':4, 'electronic circuit':2, 'plastic bar':2, 'advanced circuit':1}
timmy       = 6
cooking(name,inway,outway,stoich,timmy)

name        = 'processing unit'
inway       = ['advanced circuit', 'electronic circuit', 'sulfuric acid']
outway      = ['processing unit']
stoich      = {'advanced circuit':2, 'electronic circuit':20, 'sulfuric acid':5, 'processing unit':1}
timmy       = 10
cooking(name,inway,outway,stoich,timmy)

# Engines, drones, rocket bits and batteries
name        = 'engine unit'
inway       = ['iron gear wheel', 'pipe', 'steel plate']
outway      = ['engine unit']
stoich      = {'iron gear wheel':1, 'pipe':2, 'steel plate':1, 'engine unit':1}
timmy       = 10
cooking(name,inway,outway,stoich,timmy)

name        = 'electric engine unit'
inway       = ['electronic circuit', 'engine unit', 'lubricant']
outway      = ['electric engine unit']
stoich      = {'electronic circuit':2, 'engine unit':1, 'lubricant':16, 'electric engine unit':1}
timmy       = 10
cooking(name,inway,outway,stoich,timmy)

name        = 'flying robot frame'
inway       = ['battery', 'electric engine unit', 'electronic circuit', 'steel plate']
outway      = ['flying robot frame']
stoich      = {'battery':2, 'electric engine unit':1, 'electronic circuit':3, 'steel plate':1, 'flying robot frame':1}
timmy       = 20
cooking(name,inway,outway,stoich,timmy)

name        = 'rocket part'
inway       = ['low density structure', 'rocket control unit', 'rocket fuel']
outway      = ['rocket part']
stoich      = {'low density structure':10, 'rocket control unit':10, 'rocket fuel':10, 'rocket part':1}
timmy       = 3
cooking(name,inway,outway,stoich,timmy)

name        = 'rocket control unit'
inway       = ['processing unit', 'speed module']
outway      = ['rocket control unit']
stoich      = {'processing unit':1, 'speed module':1, 'rocket control unit':1}
timmy       = 30
cooking(name,inway,outway,stoich,timmy)

name        = 'low density structure'
inway       = ['copper plate', 'plastic bar', 'steel plate']
outway      = ['low density structure']
stoich      = {'copper plate':20, 'plastic bar':5, 'steel plate':2, 'low density structure':1}
timmy       = 20
cooking(name,inway,outway,stoich,timmy)

name        = 'battery'
inway       = ['copper plate', 'iron plate', 'sulfuric acid']
outway      = ['battery']
stoich      = {'copper plate':1, 'iron plate':1, 'sulfuric acid':20, 'battery':1}
timmy       = 4
cooking(name,inway,outway,stoich,timmy)

# Science packs
name        = 'automation science pack'
inway       = ['copper plate', 'iron gear wheel']
outway      = ['automation science pack']
stoich      = {'copper plate':1, 'iron gear wheel':1, 'automation science pack':1}
timmy       = 5
cooking(name,inway,outway,stoich,timmy)

name        = 'logistic science pack'
inway       = ['inserter', 'transport belt']
outway      = ['logistic science pack']
stoich      = {'inserter':1, 'transport belt':1, 'logistic science pack':1}
timmy       = 6
cooking(name,inway,outway,stoich,timmy)

name        = 'military science pack'
inway       = ['grenade', 'piercing rounds magazine', 'wall']
outway      = ['military science pack']
stoich      = {'grenade':1, 'piercing rounds magazine':1, 'wall':2, 'military science pack':2}
timmy       = 10
cooking(name,inway,outway,stoich,timmy)

name        = 'chemical science pack'
inway       = ['advanced circuit', 'engine unit', 'sulfur']
outway      = ['chemical science pack']
stoich      = {'advanced circuit':3, 'engine unit':2, 'sulfur':1, 'chemical science pack':2}
timmy       = 24
cooking(name,inway,outway,stoich,timmy)

name        = 'production science pack'
inway       = ['electric furnace', 'productivity module', 'rail']
outway      = ['production science pack']
stoich      = {'electric furnace':1, 'productivity module':1, 'rail':30, 'production science pack':3}
timmy       = 21
cooking(name,inway,outway,stoich,timmy)

name        = 'utility science pack'
inway       = ['flying robot frame', 'low density structure', 'processing unit']
outway      = ['utility science pack']
stoich      = {'flying robot frame':1, 'low density structure':3, 'processing unit':2, 'utility science pack':3}
timmy       = 21
cooking(name,inway,outway,stoich,timmy)

#################
### Logistics ###
#################

# Chests and Dumb Storage
name        = 'wooden chest'
inway       = ['wood']
outway      = ['wooden chest']
stoich      = {'wood':2, 'wooden chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'iron chest'
inway       = ['iron plate']
outway      = ['iron chest']
stoich      = {'iron plate':8, 'iron chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'steel chest'
inway       = ['steel plate']
outway      = ['steel chest']
stoich      = {'steel plate':8, 'steel chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'storage tank'
inway       = ['iron plate', 'steel plate']
outway      = ['storage tank']
stoich      = {'iron plate':20, 'steel plate':5, 'storage tank':1}
timmy       = 3
cooking(name,inway,outway,stoich,timmy)

# Belts
name        = 'transport belt'
inway       = ['iron gear wheel', 'iron plate']
outway      = ['transport belt']
stoich      = {'iron gear wheel':1, 'iron plate':1, 'transport belt':2}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'fast transport belt'
inway       = ['iron gear wheel', 'transport belt']
outway      = ['fast transport belt']
stoich      = {'iron gear wheel':5, 'transport belt':1, 'fast transport belt':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'express transport belt'
inway       = ['fast transport belt', 'iron gear wheel', 'lubricant']
outway      = ['express transport belt']
stoich      = {'fast transport belt':1, 'iron gear wheel':10, 'lubricant':20, 'express transport belt':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'underground belt'
inway       = ['iron plate', 'transport belt']
outway      = ['underground belt']
stoich      = {'iron plate':10, 'transport belt':5, 'underground belt':2}
timmy       = 1
cooking(name,inway,outway,stoich,timmy)

name        = 'fast underground belt'
inway       = ['iron gear wheel', 'underground belt']
outway      = ['fast underground belt']
stoich      = {'iron gear wheel':40, 'underground belt':2, 'fast underground belt':2}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

name        = 'express underground belt'
inway       = ['fast underground belt', 'iron gear wheel', 'lubricant']
outway      = ['express underground belt']
stoich      = {'fast underground belt':2, 'iron gear wheel':80, 'lubricant':40, 'express underground belt':2}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

name        = 'splitter'
inway       = ['electronic circuit', 'iron plate', 'transport belt']
outway      = ['splitter']
stoich      = {'electronic circuit':5, 'iron plate':5, 'transport belt':4, 'splitter':1}
timmy       = 1
cooking(name,inway,outway,stoich,timmy)

name        = 'fast splitter'
inway       = ['electronic circuit', 'iron gear wheel', 'splitter']
outway      = ['fast spliter']
stoich      = {'electronic circuit':10, 'iron gear wheel':10, 'splitter':1, 'fast splitter':1}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

name        = 'express splitter'
inway       = ['advanced circuit', 'fast splitter', 'iron gear wheel', 'lubricant']
outway      = ['express splitter']
stoich      = {'advanced circuit':10, 'fast splitter':1, 'iron gear wheel':10, 'lubricant':80, 'express splitter':1}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

# Inserters
name        = 'burner inserter'
inway       = ['iron gear wheel', 'iron plate']
outway      = ['burner inserter']
stoich      = {'iron gear wheel':1, 'iron plate':1, 'burner inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'inserter'
inway       = ['electronic circuit', 'iron gear wheel', 'iron plate']
outway      = ['inserter']
stoich      = {'electronic circuit':1, 'iron gear wheel':1, 'iron plate':1, 'inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'long handed inserter'
inway       = ['inserter', 'iron gear wheel', 'iron plate']
outway      = ['long handed inserter']
stoich      = {'inserter':1, 'iron gear wheel':1, 'iron plate':1, 'long handed inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'fast inserter'
inway       = ['electronic circuit', 'inserter', 'iron plate']
outway      = ['fast inserter']
stoich      = {'electronic circuit':2, 'inserter':1, 'iron plate':2, 'fast inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'filter inserter'
inway       = ['electronic circuit', 'fast inserter']
outway      = ['filter inserter']
stoich      = {'electronic circuit':4, 'inserter':1, 'filter inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'stack inserter'
inway       = ['advanced circuit', 'electronic circuit', 'inserter', 'iron gear wheel']
outway      = ['stack inserter']
stoich      = {'advanced circuit':1, 'electronic circuit':15, 'fast inserter':15, 'iron gear wheel':15, 'stack inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'stack filter inserter'
inway       = ['electronic circuit', 'stack inserter']
outway      = ['stack filter inserter']
stoich      = {'electronic circuit':5, 'stack inserter':1, 'stack filter inserter':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

# Pipes, poles and pumps
name        = 'small electric pole'
inway       = ['copper cable', 'wood']
outway      = ['small electric pole']
stoich      = {'copper cable':2, 'wood':1, 'small electric pole':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'medium electric pole'
inway       = ['copper plate', 'iron stick', 'steel plate']
outway      = ['medium electric pole']
stoich      = {'copper plate':2, 'iron stick':4, 'steel plate':2, 'medium electric pole':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'big electric pole'
inway       = ['copper plate', 'iron stick', 'steel plate']
outway      = ['big electric pole']
stoich      = {'copper plate':5, 'iron stick':8, 'steel plate':5, 'big electric pole':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'substation'
inway       = ['advanced circuit', 'copper plate', 'steel plate']
outway      = ['substation']
stoich      = {'advanced circuit':5, 'copper plate':5, 'steel plate':10, 'substation':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'pipe'
inway       = ['iron plate']
outway      = ['pipe']
stoich      = {'iron plate':1, 'pipe':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'pipe to ground'
inway       = ['iron plate', 'pipe']
outway      = ['pipe to ground']
stoich      = {'iron plate':5, 'pipe':10, 'pipe to ground':2}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'pump'
inway       = ['engine unit, pipe, steel plate']
outway      = ['pump']
stoich      = {'engine unit':1, 'pipe':1, 'steel plate':1, 'pump':1}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

# Train shit
name        = 'rail'
inway       = ['iron stick', 'steel plate', 'stone']
outway      = ['rail']
stoich      = {'iron stick':1, 'steel plate':1, 'stone':1, 'rail':2}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'train stop'
inway       = ['electronic circuit', 'iron plate', 'iron stick', 'steel plate']
outway      = ['train stop']
stoich      = {'electronic circuit':5, 'iron plate':6, 'iron stick':6, 'steel plate':3, 'train stop':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'rail signal'
inway       = ['electronic circuit', 'iron plate']
outway      = ['rail signal']
stoich      = {'electronic circuit':1, 'iron plate':5, 'rail signal':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'rail chain signal'
inway       = ['electronic circuit', 'iron plate']
outway      = ['rail chain signal']
stoich      = {'electronic circuit':1, 'iron plate':5, 'rail chain signal':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'locomotive'
inway       = ['electronic circuit', 'engine unit', 'steel plate']
outway      = ['locomotive']
stoich      = {'electronic circuit':10, 'engine unit':20, 'steel plate':30, 'locomotive':1}
timmy       = 4
cooking(name,inway,outway,stoich,timmy)

name        = 'cargo wagon'
inway       = ['iron gear wheel', 'iron plate', 'steel plate']
outway      = ['cargo wagon']
stoich      = {'iron gear wheel':10, 'iron plate':20, 'steel plate':20, 'cargo wagon':1}
timmy       = 1
cooking(name,inway,outway,stoich,timmy)

name        = 'fluid wagon'
inway       = ['iron gear wheel', 'pipe', 'steel plate', 'storage tank']
outway      = ['fluid wagon']
stoich      = {'iron gear wheel':10, 'pipe':8, 'steel plate':16, 'storage tank':1, 'fluid wagon':1}
timmy       = 1.5
cooking(name,inway,outway,stoich,timmy)

name        = 'artillery wagon'
inway       = ['advanced circuit', 'engine unit', 'iron gear wheel', 'pipe', 'steel plate']
outway      = ['artillery wagon']
stoich      = {'advanced circuit':20, 'engine unit':64, 'iron gear wheel':10, 'pipe':16, 'steel plate':40,'artillery wagon':1}
timmy       = 4
cooking(name,inway,outway,stoich,timmy)

# Vehicle stuff

# Drone stuff
name        = 'logistic robot'
inway       = ['advanced circuit', 'flying robot frame']
outway      = ['logistic robot']
stoich      = {'advanced circuit':2, 'flying robot frame':1, 'logistic robot':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'construction robot'
inway       = ['electronic circuit', 'flying robot frame']
outway      = ['construction robot']
stoich      = {'electronic circuit':2, 'flying robot frame':1, 'construction robot':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'active provider chest'
inway       = ['advanced circuit', 'electronic circuit', 'steel chest']
outway      = ['active provider chest']
stoich      = {'advanced circuit':1, 'electronic circuit':3, 'steel chest':1, 'active provider chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'passive provider chest'
inway       = ['advanced circuit', 'electronic circuit', 'steel chest']
outway      = ['passive provider chest']
stoich      = {'advanced circuit':1, 'electronic circuit':3, 'steel chest':1, 'passive provider chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'storage chest'
inway       = ['advanced circuit', 'electronic circuit', 'steel chest']
outway      = ['storage chest']
stoich      = {'advanced circuit':1, 'electronic circuit':3, 'steel chest':1, 'storage chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'buffer chest'
inway       = ['advanced circuit', 'electronic circuit', 'steel chest']
outway      = ['buffer chest']
stoich      = {'advanced circuit':1, 'electronic circuit':3, 'steel chest':1, 'buffer chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'requestor chest'
inway       = ['advanced circuit', 'electronic circuit', 'steel chest']
outway      = ['requestor chest']
stoich      = {'advanced circuit':1, 'electronic circuit':3, 'steel chest':1, 'requestor chest':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'roboport'
inway       = ['advanced circuit', 'iron gear wheel', 'steel plate']
outway      = ['roboport']
stoich      = {'advanced circuit':45, 'iron gear wheel':45, 'steel plate':45, 'roboport':1}
timmy       = 5
cooking(name,inway,outway,stoich,timmy)

# Lighting and Logic

# Bricks, concrete, landfill and cliff explosives


##################
### Production ###
##################

# Power generation/storage

# Drills, offshore pump, and oiljack

# Furnaces
name        = 'stone furnace'
inway       = ['stone']
outway      = ['stone furnace']
stoich      = {'stone':5, 'stone furnace':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'steel furnace'
inway       = ['steel plate', 'stone brick']
outway      = ['steel furnace']
stoich      = {'steel plate':6, 'stone brick':10, 'steel furnace':1}
timmy       = 3
cooking(name,inway,outway,stoich,timmy)

name        = 'electric furnace'
inway       = ['advanced circuit', 'steel plate', 'stone brick']
outway      = ['electric furnace']
stoich      = {'advanced circuit':5, 'steel plate':10, 'stone brick':10, 'electric furnace':1}
timmy       = 5
cooking(name,inway,outway,stoich,timmy)

# Crafty machines and labs
name        = 'assembling machine 1'
inway       = ['electronic circuit', 'iron gear wheel', 'iron plate']
outway      = ['assembline machine 1']
stoich      = {'electronic circuit':3, 'iron gear wheel':5, 'iron plate':9, 'assembling machine 1':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'assembling machine 2'
inway       = ['assembling machine 1', 'electronic circuit', 'iron gear wheel', 'steel plate']
outway      = ['assembling machine 2']
stoich      = {'assembling machine 1':1, 'electronic circuit':3, 'iron gear wheel':5, 'steel plate':2, 'assembling machine 2':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'assembling machine 3'
inway       = ['assembling machine 2', 'speed module']
outway      = ['assembling machine 3']
stoich      = {'assembling machine 2':2, 'speed module':4, 'assembling machine 3':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)

name        = 'oil refinery'
inway       = ['electronic circuit', 'iron gear wheel', 'pipe', 'steel plate', 'stone brick']
outway      = ['oil refinery']
stoich      = {'electronic circuit':10, 'iron gear wheel':10, 'pipe':10, 'steel plate':15, 'stone brick':10, 'oil refinery':1}
timmy       = 8
cooking(name,inway,outway,stoich,timmy)

name        = 'chemical plant'
inway       = ['electronic circuit', 'iron gear wheel', 'pipe', 'steel plate']
outway      = ['chemical plant']
stoich      = {'electronic circuit':5, 'iron gear wheel':5, 'steel plate':5, 'chemical plant':1}
timmy       = 5
cooking(name,inway,outway,stoich,timmy)

name        = 'centrifuge'
inway       = ['advanced circuit', 'concrete', 'iron gear wheel', 'steel plate']
outway      = ['centrifuge']
stoich      = {'advanced circuit':100, 'concrete':100, 'iron gear wheel':100, 'steel plate':50, 'centrifuge':1}
timmy       = 4
cooking(name,inway,outway,stoich,timmy)

name        = 'lab'
inway       = ['electronic circuit', 'iron gear wheel', 'transport belt']
outway      = ['lab']
stoich      = {'electronic circuit':10, 'iron gear wheel':10, 'transport belt':4, 'lab':1}
timmy       = 2
cooking(name,inway,outway,stoich,timmy)

# Modules
name        = 'beacon'
inway       = ['advanced circuit', 'copper cable', 'electronic circuit', 'steel plate']
outway      = ['beacon']
stoich      = {'advanced circuit':20, 'copper cable':10, 'electronic circuit':20, 'steel plate':10, 'beacon':1}
timmy       = 15
cooking(name,inway,outway,stoich,timmy)

name        = 'speed module'
inway       = ['advanced circuit', 'electronic circuit']
outway      = ['speed module']
stoich      = {'advanced circuit':5, 'electronic circuit':5, 'speed module':1}
timmy       = 15
cooking(name,inway,outway,stoich,timmy)


# Rocket related


##############
### Combat ###
##############

# Guns and mines

# Ammo
name        = 'firearm magazine'
inway       = ['iron plate']
outway      = ['firearm magazine']
stoich      = {'iron plate':4, 'firearm magazine':1}
timmy       = 1
cooking(name,inway,outway,stoich,timmy)

name        = 'piercing rounds magazine'
inway       = ['copper plate', 'firearm magazine', 'steel plate']
outway      = ['piercing rounds magazine']
stoich      = {'copper plate':5, 'firearm magazine':1, 'steel plate':1, 'piercing rounds magazine':1}
timmy       = 3
cooking(name,inway,outway,stoich,timmy)


# G'nades and capsules
name        = 'grenade'
inway       = ['coal', 'iron plate']
outway      = ['grenade']
stoich      = {'coal':10, 'iron plate':5, 'grenade':1}
timmy       = 8
cooking(name,inway,outway,stoich,timmy)


# Armor

# Grid stuff

# Grid combat stuff

# Walls, turrets and radars
name        = 'wall'
inway       = ['stone brick']
outway      = ['wall']
stoich      = {'stone brick':5, 'wall':1}
timmy       = 0.5
cooking(name,inway,outway,stoich,timmy)



# name        = ''
# inway       = []
# outway      = []
# stoich      = {}
# timmy       = 0.5
# cooking(name,inway,outway,stoich,timmy)


