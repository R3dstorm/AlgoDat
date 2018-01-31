#!/usr/bin/python3

from graph import Graph
import timeit


def measure_runtime():
    return


def evaluate_graph(graph_file, start_point, end_point, generate_map):
    """

    :param graph_file:
    :param start_point:
    :param end_point:
    :param generate_map:
    :return:

    >>> evaluate_graph('test3.graph', 0, 3, True)
    []
    """
    active_graph = Graph()
    active_graph.read_graph_from_file(graph_file)
    if generate_map is True:
        MAP_OUT = open("output.map", "w")
        MAP_OUT.write('[map]\n')


    # Compute and measure runtime:
    # 1. Distance
    active_graph.set_arc_costs_to_distance()
    active_graph.compute_shortest_paths(start_point)
    costs = active_graph.get_node_cost(end_point)
    if generate_map is True:
        string = active_graph.generate_map_data(end_point, 'blue', 'shortest path')
        MAP_OUT.write(string + ';\n')
    # TODO Runtime:...

    # 2. Travel time automotive
    active_graph.set_arc_costs_to_travel_time(130)
    active_graph.reset_graph()
    active_graph.compute_shortest_paths(start_point)
    if generate_map is True:
        string = active_graph.generate_map_data(end_point, 'red', 'travel time car')
        MAP_OUT.write(string + ';\n')
    # TODO Runtime:...

    # 3. Travel time moped
    active_graph.set_arc_costs_to_travel_time(100)
    active_graph.reset_graph()
    active_graph.compute_shortest_paths(start_point)
    if generate_map is True:
        string = active_graph.generate_map_data(end_point, 'green', 'travel time moped')
        MAP_OUT.write(string)
    # TODO Runtime:...

    #Print data:
    # print('the shortest path between %d and %d has a distance of: %d km \n' % ())
    # print('computation time: %f s \n' % ())
    # print('the fastest traveling time by car (max. speed 130 km/h) is: %d hour(s) %d minute(s) \n' % ())
    # print('computation time: %f s \n' % ())
    # print('the fastest traveling time by tuned moped (max. speed 100 km/h) is: %d hour(s) %d minute(s) \n' % ())
    # print('computation time: %f s \n' % ())

    if generate_map is True:
        MAP_OUT.write('[/map]')
        MAP_OUT.close()


if __name__ == "__main__":
    graph = Graph()
    # graph.read_graph_from_file('bawue_bayern.graph')
    graph.read_graph_from_file('test3.graph')
    graph.compute_shortest_paths(0)


    blub = 1
