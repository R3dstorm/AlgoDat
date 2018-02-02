#!/usr/bin/python3

from graph import Graph
import timeit


def measure_runtime():
    return


def format_time(time_s):
    hours = time_s // 3600
    minutes = (time_s % 3600) / 60
    return hours, minutes


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
    runtime_output = open('runtime.txt', 'w')
    active_graph = Graph()
    active_graph.read_graph_from_file(graph_file)
    print("File read in\n")

    # Compute and measure runtime:
    # 1. Distance
    runtime_output.write("Traveling from Faculty of Engineering to Nuernberg:\n\n")
    active_graph.set_arc_costs_to_distance()
    runtime = timeit.timeit(stmt=lambda: active_graph.compute_shortest_paths(start_point), number=1)
    travel_distance = active_graph.get_node_cost(end_point)/1000
    active_graph.set_arc_costs_to_travel_time(1000)
    travel_time = format_time(active_graph.recalculate_travel_costs(end_point))

    print("Traveling shortest path: %.2f km\n" % travel_distance)
    runtime_output.write("Shortest path:\n")
    runtime_output.write("Traveling distance of %.2f km, Traveling time of %d hour(s) %d minute(s); Runtime for computing: %.2f s \n\n" % (travel_distance, travel_time[0], travel_time[1], runtime))
    if generate_map is True:
        active_graph.print_to_map_data(end_point, 'blue', 'shortest path', True)

    # 2. Travel time automotive
    active_graph.set_arc_costs_to_travel_time(130)
    active_graph.reset_graph()
    runtime = timeit.timeit(stmt=lambda: active_graph.compute_shortest_paths(start_point), number=1)
    travel_time = format_time(active_graph.get_node_cost(end_point))
    furthest = active_graph.calculate_furthest_node()
    travel_time_long = format_time(furthest[1])
    active_graph.set_arc_costs_to_distance()
    travel_distance = active_graph.recalculate_travel_costs(end_point)/1000
    travel_distance_long = active_graph.recalculate_travel_costs(furthest[0])/1000

    print("Traveling by car (fastest): %.2f km\n" % travel_distance)
    runtime_output.write("Fastest path by car:\n")
    runtime_output.write("Traveling distance of %.2f km, Traveling time of %d hour(s) %d minute(s); Runtime for computing: %.2f s \n" % (travel_distance, travel_time[0], travel_time[1], runtime))
    runtime_output.write("Longest path by car:\n")
    runtime_output.write("Traveling distance of %.2f km, Traveling time of %d hour(s) %d minute(s)\n\n" % (travel_distance_long, travel_time_long[0], travel_time_long[1]))
    if generate_map is True:
        active_graph.print_to_map_data(end_point, 'blue', 'traveling by car', True)


    # 3. Travel time moped
    active_graph.set_arc_costs_to_travel_time(100)
    active_graph.reset_graph()
    runtime = timeit.timeit(stmt=lambda: active_graph.compute_shortest_paths(start_point), number=1)
    travel_time = format_time(active_graph.get_node_cost(end_point))
    furthest = active_graph.calculate_furthest_node()
    travel_time_long = format_time(furthest[1])
    active_graph.set_arc_costs_to_distance()
    travel_distance = active_graph.recalculate_travel_costs(end_point)/1000
    travel_distance_long = active_graph.recalculate_travel_costs(furthest[0])/1000

    print("Traveling by moped (fastest): %.2f km\n" % travel_distance)
    runtime_output.write("Fastest path by moped:\n")
    runtime_output.write("Traveling distance of %.2f km, Traveling time of %d hour(s) %d minute(s); Runtime for computing: %.2f s \n" % (travel_distance, travel_time[0], travel_time[1], runtime))
    runtime_output.write("Longest path by car:\n")
    runtime_output.write("Traveling distance of %.2f km, Traveling time of %d hour(s) %d minute(s)\n" % (travel_distance_long, travel_time_long[0], travel_time_long[1]))
    if generate_map is True:
        active_graph.print_to_map_data(end_point, 'blue', 'traveling by moped', True)

    runtime_output.close()

if __name__ == "__main__":
    evaluate_graph('bawue_bayern.graph', 5508637, 4435496, True)
