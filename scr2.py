import os
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3

with Diagram('waddup dude', outformat='jpg',direction='TB'):
    l1 = ELB(f'electronic_circuit')
    # l1>>EC2('weeb')>>ELB('dog')
    # l1>>EC2('weeb')>>ELB('kitty')


    lists = [[3,2,2,4,4,5],[1,2,3],[22,4,6]]

    for i in lists:
        local = []
        for g in i:
            local.append(EC2(g))
        l1>>local