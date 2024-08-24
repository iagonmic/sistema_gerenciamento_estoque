class Graph:

    def __init__(self):
        self.structure = {}

    def get_nodes(self, origin):
        if origin in self.structure:
            return self.structure.get(origin)
        
        return []
    
    def add_graph(self, origin, end, ordened: bool):
        nodes = self.get_nodes(origin)
        nodes.append(end)
        
        self.structure[origin] = nodes

        if not ordened:
            self.add_graph(end, origin, True)