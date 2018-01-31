#!/usr/bin/python3

import re
import queue


class Graph:

    def __init__(self):
        self._num_nodes = 0
        self._num_arcs = 0
        # List for storing node objects.
        self._nodes = []
        # List of lists for storing edge objects for each node.
        self._adjacency_lists = []

    def read_graph_from_file(self, file_name):
        """ Read in graph from .graph file.

        Specification of .graph file format:
            First line: number of nodes
            Second line: number of arcs
            3-column lines with node information:
                node_id latitude longitude
            4-column lines with edge information:
                tail_node_id head_node_id distance(m) max_speed(km/h)
        Comment lines (^#) are ignored

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test.graph")
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        c_lines = 0
        with open(file_name) as f:
            for line in f:
                cols = line.strip().split(" ")
                # Skip comment lines.
                if re.search("^#", cols[0]):
                    continue
                c_lines += 1
                if c_lines == 1:
                    if self._num_nodes != 0:
                        raise Exception("Graph already read in")
                    self._num_nodes = int(cols[0])
                elif c_lines == 2:
                    self._num_arcs = int(cols[0])
                elif c_lines <= self._num_nodes + 2:  # all node info lines.
                    if not len(cols) == 3:
                        raise Exception("Node info line with != 3 cols")
                    node = Node(int(cols[0]), float(cols[1]), float(cols[2]))
                    # Append node to list.
                    self._nodes.append(node)
                    # Append empty adjacency list for node.
                    self._adjacency_lists.append([])
                else:  # all arc info lines.
                    if not len(cols) == 4:
                        raise Exception("Arc info line with != 4 cols")
                    tail_node_id = int(cols[0])
                    arc = Arc(tail_node_id, int(cols[1]), int(cols[2]),
                              int(cols[3]))
                    # Append arc to tail node's adjacency list.
                    self._adjacency_lists[tail_node_id].append(arc)
        f.close()

    def get_num_nodes(self):
        """Return number of nodes in graph."""
        return self._num_nodes

    def get_num_arcs(self):
        """Return number of arcs in graph."""
        return self._num_arcs

    def compute_reachable_nodes(self, node_id):
        """Mark all nodes reachable from given node.

        Implemented as breadth first search (BFS)
        Returns the number of reachable nodes (incl. start node)

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test2.graph")
        >>> marked_nodes = []
        >>> graph.compute_reachable_nodes(0)[0]
        4
        >>> graph.compute_reachable_nodes(4)[0]
        6
        >>> graph.compute_reachable_nodes(6)[0]
        1
        """
        # List of nodes to visit currently.
        current_level = [node_id]
        # Create list of marked nodes, marking reachable nodes with 1.
        marked_nodes = [0] * self._num_nodes
        marked_nodes[node_id] = 1  # Mark start node as reachable.
        num_marked_nodes = 1  # Store number of reachable nodes.
        # While there are still nodes to visit.
        while len(current_level) > 0:
            # Store nodes that are connected to current_level nodes.
            next_level = []
            # Go through all current_level nodes.
            for curr_node_id in current_level:
                # Go through arcs of current node.
                for arc in self._adjacency_lists[curr_node_id]:
                    # If head_id not marked yet.
                    if not marked_nodes[arc.head_node_id]:
                        marked_nodes[arc.head_node_id] = 1
                        num_marked_nodes += 1
                        # Add head_id to new current level nodes.
                        next_level.append(arc.head_node_id)
            current_level = next_level
        return num_marked_nodes, marked_nodes

    def set_arc_costs_to_travel_time(self, max_vehicle_speed):
        """Set arc costs to travel time in whole seconds.

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test.graph")
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph
        [0->1(4), 0->2(8), 1->2(2), 2->3(6), 3->1(5), 4->3(2)]
        """
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                # Compute max possible speed for this arc.
                max_speed = min(arc.max_speed, int(max_vehicle_speed))
                # Compute travel time in whole seconds.
                travel_time_sec = "%.0f" % (arc.distance / (max_speed / 3.6))
                # Set costs to travel time in whole seconds.
                arc.costs = int(travel_time_sec)

    def set_arc_costs_to_distance(self):
        """Set arc costs to distance.

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test.graph")
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        >>> graph.set_arc_costs_to_travel_time(100)
        >>> graph.set_arc_costs_to_distance()
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                arc.costs = arc.distance

    def compute_lcc(self):
        """Mark all nodes in the largest connected component.

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test2.graph")
        >>> marked_nodes = []
        >>> graph.compute_lcc()
        [1, 2, 3, 4, 5, 6]
        """

        # Step 1: find starting point, spanning largest component from all nodes:
        lcc = (0, [])
        start_node_id_lcc = 0
        for current_node in range(0, self._num_nodes):
            temp_size = self.compute_reachable_nodes(current_node)
            if temp_size[0] > lcc[0]:
                lcc = temp_size
                start_node_id_lcc = current_node
        # Step 1 Improvements: only scan points, that have not been marked yet...

        # Step 2: return list with all nodes resulting from MVS within the function argument
        result = []
        for i in range(0, len(lcc[1])):
            if lcc[1][i] == 1:
                result.append(i)
        return result

    def compute_shortest_paths(self, start_node_id):
        """Compute the shortest paths for a given start node
        using Dijkstra's algorithm.

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph')
        >>> graph.compute_shortest_paths(0)
        >>> ['%d(%d)' % (node._id, node._distance) for node in graph._nodes]
        ['0(0)', '1(30)', '2(50)', '3(100)', '4(-1)']
        >>> [repr(node._traceback_arc) for node in graph._nodes]
        ['0->0(0)', '0->1(30)', '1->2(20)', '2->3(50)', '0->0(0)']
        >>> graph = Graph()
        >>> graph.read_graph_from_file('test3.graph')
        >>> graph.compute_shortest_paths(0)
        >>> ['%d(%d)' % (node._id, node._distance) for node in graph._nodes]
        ['0(0)', '1(70)', '2(50)', '3(60)']
        >>> [repr(node._traceback_arc) for node in graph._nodes]
        ['0->0(0)', '3->1(10)', '0->2(50)', '2->3(10)']
        """
        node_queue = queue.PriorityQueue(self._num_nodes)

        # Start of search with start node:
        current_node = self._nodes[start_node_id]
        current_node._settled = True
        current_node._distance = 0

        # Insert next neighbored nodes into priority queue
        current_distance = 0
        while True:
            size = len(self._adjacency_lists[int(repr(current_node))])
            for neighbor in range(size):
                current_arc = self._adjacency_lists[int(repr(current_node))][neighbor]
                next_node = self._nodes[current_arc.head_node_id]
                if not next_node.is_settled():
                    # Store traceback information
                    next_node.set_traceback_arc(current_arc)
                # insert if node has not been inserted, or inserted with a bigger key
                if (next_node.get_distance() == -1) or next_node.get_distance() > current_distance + current_arc.costs:
                    if not next_node.is_settled():  # Insert node if not already settled
                        next_node.set_distance(current_distance + current_arc.costs)  # Passing costs to next node
                        node_queue.put_nowait((next_node.get_distance(), next_node))
            if not node_queue.empty():
                current_node = node_queue.get_nowait()[1]  # Deque element and remove key-information
                if not current_node.is_settled():  # Reject outdated (higher distance) nodes from the queue
                    # Settle node
                    current_node.settle()
                    current_distance = current_node.get_distance()
            else:
                break

    def get_node_cost(self, node):
        return self._nodes[node].get_distance()

    def generate_map_data(self, end_node, color, label):
        """
        Returns a "MapBBCode" formatted string starting from end
        Format: <lat11>,<lon11> <lat12>,<lon12> ... <lat1n>,<lon1n>(color/label1);
        :return: MapBBCode formatted string

        >>> graph = Graph()
        >>> graph.read_graph_from_file('test.graph')
        >>> graph.compute_shortest_paths(0)
        >>> graph.generate_map_data(3, 'blue', 'route66')
        '49.265800,7.311790 49.266600,7.311080 49.340600,7.299970 49.341800,7.300890(blue|route66)'

        """
        string = ''
        current_node = self._nodes[end_node]
        while True:
            temp = '%f,%f' % (current_node.get_latitude(), current_node.get_longitude())
            string += temp
            # Set next node for current_node:
            next_node = self._nodes[current_node.get_traceback_arc().tail_node_id]
            if (next_node != current_node):
                current_node = next_node
                string += ' '
            else:
                break
        string = ''.join([string, '(',color, '|', label, ')'])
        return string

    def reset_graph(self):
        for node in self._nodes:
            node.reset_node()


    def __repr__(self):
        """ Define object's string representation.

        >>> graph = Graph()
        >>> graph.read_graph_from_file("test.graph")
        >>> graph
        [0->1(30), 0->2(70), 1->2(20), 2->3(50), 3->1(40), 4->3(20)]
        """
        obj_str_repr = ""
        for i in range(self._num_nodes):
            for arc in self._adjacency_lists[i]:
                obj_str_repr += repr(arc) + ", "
        if obj_str_repr:
            return "[" + obj_str_repr[:-2] + "]"
        else:
            return "[]"


class Node:

    def __init__(self, node_id, latitude, longitude):
        self._id = node_id
        self._latitude = latitude
        self._longitude = longitude
        self._traceback_arc = Arc(0, 0, 0, 0)
        self._settled = False
        self._distance = -1  # Distance from a certain starting point; Init with negative distance

    def __repr__(self):
        """ Define object's string representation."""
        return "%i" % self._id

    def reset_node(self):
        self._traceback_arc = Arc(0, 0, 0, 0)
        self._settled = False
        self._distance = -1

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def settle(self):
        self._settled = True

    def is_settled(self):
        return self._settled is True

    def set_distance(self, distance):
        self._distance = distance

    def get_distance(self):
        return self._distance

    def set_traceback_arc(self, arc):
        self._traceback_arc = arc

    def get_traceback_arc(self):
        return self._traceback_arc

class Arc:

    def __init__(self, tail_id, head_id, distance, max_speed):
        self.tail_node_id = tail_id  # ID of tail node.
        self.head_node_id = head_id  # ID of head node.
        self.distance = distance  # Distance in meter.
        self.max_speed = max_speed  # Maximum speed.
        self.costs = distance  # Set default costs to distance.

    def __repr__(self):
        """ Define object's string representation."""
        return "%i->%i(%i)" % (self.tail_node_id, self.head_node_id,
                               self.costs)
