import numpy as np
class Graph:
    def __init__(self, node_num, starting_node = 1):
        '''
            the parameters required for initialize graph and prim algorithm 
            parameter:
                node_num = node num in this graph
                starting_node : 1 to node_num
        '''
        self.starting_node = starting_node - 1                  #strating node 
        self.mcmt = [starting_node - 1]                         #selected nodes
        self.mcmt_link = []                                     #selected edges
        self.node_num = int(node_num)
        self.martix = np.zeros((node_num, node_num))            #initialize Adjacency Matrix  with numpy array
    #Add edge
    def add_link(self, node1, node2, weight):
        self.martix[node1, node2] = weight
        self.martix[node2, node1] = weight
    #prim algorithm implment
    def prim(self, node):           
        buffer = []
        for node1 in self.mcmt:
            self.connect_nodes = self.martix[node1]
            self.sroted_nodes = np.argsort(self.connect_nodes)
            for node2 in self.sroted_nodes:
                if node2 not in self.mcmt and self.connect_nodes[node2] != 0:
                    buffer.append((node1,node2))
                    break
        min_weight = self.martix[buffer[0]]
        min_link = buffer[0]
        node = buffer[0][1]
        for link in buffer:
            weight = self.martix[link]
            if weight < min_weight:
                min_weight = weight
                node = link[1]
                min_link = link
        self.mcmt.append(node)
        self.mcmt_link.append((min_link[0] + 1, min_link[1] + 1))
        if len(self.mcmt) == self.node_num:
            return
        # print(buffer)
        self.prim(node)
#test
if __name__ == "__main__":
    graph = Graph(6,1)
    graph.add_link(0, 1, 6)
    graph.add_link(0, 2, 1)
    graph.add_link(0, 3, 5)
    graph.add_link(1, 2, 5)
    graph.add_link(1, 4, 3)
    graph.add_link(2, 4, 6)
    graph.add_link(2, 3, 5)
    graph.add_link(2, 5, 4)
    graph.add_link(3, 5, 2)
    graph.add_link(4, 5, 6)
    print(graph.martix)
    graph.prim(graph.starting_node)
    print([node + 1 for node in graph.mcmt])
    print(graph.mcmt_link)