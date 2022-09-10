class Graph:
    def __init__(self):
        self.nodes_number = 0
        self.adjacent_list = {}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self, node):
        # check input
        if not node:
            print("wrong input")
            return
        # check if node already exists
        # then do not add it
        if self.adjacent_list.get(node):
            print(f"{node} already exists in graph")
            return
        self.adjacent_list[node] = []
        self.nodes_number += 1

    def add_edge(self, node1, node2):
        # check input
        if not node1 or not node2:
            print("wrong input")
            return
        # check if nodes exist in graph
        if node1 in self.adjacent_list and node2 in self.adjacent_list:
            # then add in adjacent list nodes:
            # for key=node1 in adjacent_list add in value(array) node2 and
            self.adjacent_list[node1].append(node2)
            # for key=node2 in adjacent_list add in value(array) node1 and
            self.adjacent_list[node2].append(node1)
            return
        # else return that wrong edge
        print("wrong edge")
        return

    def show_connections(self):
        """
        Print nodes and their connections
        :return:
        """
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            print(f"{node} --> {' '.join(node_connections)}")


my_graph = Graph()
my_graph.add_vertex('0')
my_graph.add_vertex('1')
my_graph.add_vertex('2')
my_graph.add_vertex('3')
my_graph.add_vertex('4')
my_graph.add_vertex('5')
my_graph.add_vertex('6')

print(my_graph)

my_graph.add_edge('3', '1')
my_graph.add_edge('3', '4')
my_graph.add_edge('4', '2')
my_graph.add_edge('4', '5')
my_graph.add_edge('1', '2')
my_graph.add_edge('1', '0')
my_graph.add_edge('0', '2')
my_graph.add_edge('6', '5')
print(my_graph)
my_graph.show_connections()
