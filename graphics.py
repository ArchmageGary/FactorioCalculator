import os
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Factory", show=False):
    ELB("Factorio") >> EC2("???") >> RDS("profit")