class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.__nodes = nodes
        self.__edges = edges
        self.__root = None

    def get_node(self, name):
        for node in self.__nodes:
            if node.get_name() == name:
                return node
        return None

    def get_nodes(self):
        return self.__nodes
    
    def get_edges(self):
        return self.__edges

    def get_root(self):
        return self.__root
    
    def add_node(self, node):
        self.__nodes.append(node)
        if not self.__root:
            self.__root = node

    def add_edge(self, node1, node2):
        self.__edges.append((node1, node2))

    def __str__(self):
        nodes = "".join([str(node) + "\n" for node in self.__nodes])
        edges = "".join([str(edge) + "\n" for edge in self.__edges])
        return "Nodes: " + nodes + "\nEdges: " + edges

    def get_children(self, node):
        return [edge[1] for edge in self.__edges if edge[0] == node]
    
    def get_parents(self, node):
        return [edge[0] for edge in self.__edges if edge[1] == node]