from graph import Graph

class BayesianNetwork:
    def __init__(self):
        self.graph = Graph()

    def add_state(self, state):
        self.graph.add_node(state)

    def add_states(self, *states):
        for state in states:
            self.graph.add_node(state)

    def add_edge(self, state1, state2):
        self.graph.add_edge(state1, state2)

    def __str__(self):
        return str(self.graph)
    
    def probability(self, state):
        p = 1
        for key, value in state.items():
            node = self.graph.get_node(key)
            try:
                distribution = node.get_distribution()
            except:
                raise Exception(f'Node {key} is not defined')
            if distribution == 'discrete':
                p *= node.get_cpt()[value]
            else:
                parents = self.graph.get_parents(node)
                try:
                    parents_values = [state[parent.get_name()] for parent in parents]
                except:
                    raise Exception(f'Conditional probability table for {node.get_name()} is not complete')
                cpt = node.get_cpt()
                curr_state = parents_values + [value]
                for row in cpt:
                    if row[:-1] == curr_state:
                        p *= row[-1]
                        break
        return round(p, 5)
    