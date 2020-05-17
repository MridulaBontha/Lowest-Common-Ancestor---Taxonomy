import csv
from sys import argv

def parse_tree(nodefile):
    # create a child and parent dictionary
    child_parent_dict = {}
    # dictionary to hold rank of each of the node in the tree
    node_rank = {}
    with open(nodefile, "r") as nodes:
        data_reader = csv.reader(nodes, delimiter='|')
        for line in data_reader:
            child, parent, rank = int(line[0].strip()), int(line[1].strip()), line[2].strip()
            child_parent_dict[child] = parent
            node_rank[child] = rank
    return child_parent_dict,node_rank


def taxid_to_name(name_file):
    taxid_name_dict = {}
    with open(name_file, "r") as nodes:
        data_reader = csv.reader(nodes,delimiter='|')
        for line in data_reader:
            taxid, name, name_class = int(line[0].strip()), line[1].strip(), line[3].strip()
            # keeping a track of scientific names associated with each tax-id
            if name_class == "scientific name":
                taxid_name_dict[taxid] = name
    return taxid_name_dict


# method to fetch first common ancestor irrespective of rank type ( un-ranked )
def get_first_common_element_unranked(ancestor_list_1, ancestor_list_2):

    for ancestor in ancestor_list_1:
        if ancestor in ancestor_list_2:
            return ancestor
    return None

# method to fetch first common ancestor with respect to rank type


def get_first_common_element_ranked(ancestor_list_1, ancestor_list_2, rank_level, node_rank):
    for ancestor in ancestor_list_1:
        if ancestor in ancestor_list_2 and (node_rank[ancestor] == rank_level):
            return ancestor
    return None


def return_ancestor(taxid1, taxid2, rank_level=None,ranked=False):
    child_parent_dict, node_rank = parse_tree(node_file)
    # list to hold the ancestors of the first node-id
    list_parents_1 = []
    # dictionary to hold ranks of all the ancestors
    ranks = {}
    # list to hold the ancestors of the second node-id
    list_parents_2 = []
    parent1 = child_parent_dict[taxid1]
    parent2 = child_parent_dict[taxid2]
    # add ancestors to the list until you reach the root node
    while parent1 != 1:
        parent1 = child_parent_dict[parent1]
        list_parents_1.append(parent1)
        ranks[parent1] = node_rank[parent1]
    # add ancestors to the list until you reach the root node
    while parent2 != 1:
        parent2 = child_parent_dict[parent2]
        list_parents_2.append(parent2)
        ranks[parent2] = node_rank[parent2]
    if ranked:
        return get_first_common_element_ranked(list_parents_1, list_parents_2, rank_level,ranks)
    else:
        return get_first_common_element_unranked(list_parents_1, list_parents_2)


if __name__ == '__main__':
    node_file = argv[1]
    name_file = argv[2]
    taxid_name_dict = taxid_to_name(name_file)
    taxid1 = int(argv[3])
    taxid2 = int(argv[4])
    rank_level = None
    ranked = False
    if len(argv) > 5:
        rank_level = argv[5]
        ranked = True

    common_ancestor = taxid_name_dict[return_ancestor(taxid1, taxid2, rank_level, ranked=ranked)]
    print("Lowest common ancestor between "+taxid_name_dict[taxid1]+" and "+taxid_name_dict[taxid2]+" is "+common_ancestor)


