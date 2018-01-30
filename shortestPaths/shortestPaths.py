#!/usr/bin/python3

from graph import Graph







if __name__ == "__main__":
    graph = Graph()
 #   graph.read_graph_from_file('bawue_bayern.graph')
    graph.read_graph_from_file('test.graph')
    graph.compute_shortest_paths(0)
    nodes = graph.compute_reachable_nodes(0)
    blub = 1