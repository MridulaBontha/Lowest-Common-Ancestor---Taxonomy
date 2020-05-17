# Lowest-Common-Ancestor-Taxonomy

The Python script lowest_common_ancestor provides the lowest common ancestor between two given organism.
The user needs to input the taxids of both the organisms. It is optional to provide the rank at which the ancestor has to found.

REQUIREMENTS
------------

This module requires Python3 installation.

The arguments to the script are as follows :
python3 lowest_common_ancestor.py <path to nodes.dmp> < path to names.dmp> <taxid1> <taxid2> <rank-level-optional>
  
# Some sample output:
```
python3 lowest_common_ancestor.py.py nodes.dmp names.dmp 9931 9954 class
Lowest common ancestor between Damaliscus pygargus and Cephalophus is Mammalia

python3 lowest_common_ancestor.py.py nodes.dmp names.dmp 9931 9954
Lowest common ancestor between Damaliscus pygargus and Cephalophus is Bovidae
```
