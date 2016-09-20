
class Graph:

    def __init__(self, nodes_and_edges={}):
        self.nodes_dict = dict(nodes_and_edges)

    def get_adjlist(self, node):
        if node in self.nodes_dict:
            return self.nodes_dict[node]
        else:
            return None

    def is_adjacent(self, node1, node2):
        if node1 in self.nodes_dict:
            if node2 in self.nodes_dict[node1]:
                return True
            else:
                return False
        elif node2 in self.nodes_dict:
            if node1 in self.nodes_dict[node2]:
                return True
            else:
                return False
        else:
            return False

    def num_nodes(self):
        return len(self.nodes_dict)

    def __str__(self):
        return str(self.nodes_dict)

    def __iter__(self):
        return iter(self.nodes_dict)

    def __contains__(self, node):
        return node in self.nodes_dict

    def __len__(self):
        return len(self.nodes_dict)

    def add_node(self, node):
        if node in self:
            return False
        else:
            self.nodes_dict[node] = []
            return True

    def link_nodes(self, node1, node2):
        if node1 in self and node2 in self:
            if self.is_adjacent(node1, node2):
                return False
            elif node1 is not node2:
                self.nodes_dict[node1].append(node2)
                self.nodes_dict[node2].append(node1)
                return True
        else:
            return False

    def unlink_nodes(self, node1, node2):
        if node1 in self and node2 in self:
            if self.is_adjacent(node1, node2):
                self.nodes_dict[node1].remove(node2)
                self.nodes_dict[node2].remove(node1)
                return True
            else:
                return False
        else:
            return False

    def del_node(self, node):
        if node in self:
            for other_node in self:
                if other_node is not node:
                    self.unlink_nodes(node, other_node)
            self.nodes_dict.pop(node)
            return True
        else:
            return False
