import networkx as nx
import os

class Graph:
    # n = num vertices, p = probability for each edge
    def __init__(self, edges):
        '''
        INPUT: edges - tuple of tuples (start_node, end_node, weight)
        '''   
        self.graph = nx.DiGraph()
        self.graph.add_weighted_edges_from(edges)  
        self.nodes = self.graph.nodes   
        self.edges = self.edge_table(edges)

    def edge_table(self, edges):

        table = dict()
        updated = dict()
        for i in range(len(edges)):
            key = edges[i][0]
            value = {edges[i][1]:edges[i][2]}
            update_key = list(value.keys())[0]
            updated = table.get(key, dict())
            updated.update({update_key: value[update_key]})
            table.update({key:updated})

        return table


    def print_graph(self):
        for row in self.graph:
            print(row)


    def plot_graph(self):
        '''
            Description: Plots the graph in a circular set of nodes
            INPUT: None
            OUTPUT: A matplotlib plot of the graph 
        '''
        '''# Credit: https://stackoverflow.com/questions/44271504/given-an-adjacency-matrix-how-to-draw-a-graph-with-matplotlib
        # graph_plot = nx.from_numpy_array(self.graph)
        # nx.draw_circular(self.graph, with_labels = True, arrows = True)
        # plt.axis('equal')
        #pos = nx.get_node_attributes(self.graph, 'pos')
        
        
        # Credit: https://stackoverflow.com/questions/28372127/add-edge-weights-to-plot-output-in-networkx
        # pos = nx.spring_layout(self.graph)

        # nx.draw_networkx_nodes(self.graph, pos)
        # nx.draw_networkx_labels(self.graph, pos)
        # nx.draw_networkx_edges(self.graph, pos, connectionstyle='arc3, rad = 0.2')

        # labels = nx.get_edge_attributes(self.graph, 'weight')
        # nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = labels)
        # plt.show()'''

        graphviz = nx.drawing.nx_agraph.to_agraph(self.graph)
        for u, v, d in self.graph.edges(data=True):
            graphviz.get_edge(u, v).attr['label'] = d['weight']

        output_dir = os.path.join(os.getcwd(), 'frontend', 'public')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'graph.png')

        graphviz.draw(output_path, prog='dot', format='png')
        os.startfile(output_path)
        print('plotted')

    def draw_tsp(self, path):
        graphviz = nx.drawing.nx_agraph.to_agraph(self.graph)

        nodelist = list(path)
        # pathlist = [(nodelist[i], nodelist[i+1]) for i in range(len(nodelist)-1)]

        for i in range(len(nodelist)-1):
            graphviz.get_node(nodelist[i]).attr['fillcolor'] = 'red'
            edge = graphviz.get_edge(nodelist[i], nodelist[i+1])
            edge.attr['color'] = 'red'
            edge.attr['width'] = 3
        graphviz.get_node(nodelist[len(nodelist)-1]).attr['fillcolor'] = 'red'

        output_dir = os.path.join(os.getcwd(), 'frontend', 'public')
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, 'tsp.png')

        graphviz.draw(output_path, prog='dot', format='png')
        os.startfile('tsp.png')
        print('solved')

            









