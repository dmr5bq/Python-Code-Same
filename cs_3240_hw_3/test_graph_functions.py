import unittest
from graph_functions import *


class TestGraphFunctions(unittest.TestCase):

    def test_is_complete(self):
        graph = Graph()

        self.assertTrue(is_complete(graph))

        graph.add_node(0)

        self.assertTrue(is_complete(graph))

        graph.add_node(1)

        self.assertFalse(is_complete(graph))

        graph.link_nodes(0,1)

        self.assertTrue(is_complete(graph))

        graph = Graph()

        for i in range(0,10):
            graph.add_node(i)

        for node in graph:
            for other_node in graph:
                graph.link_nodes(node, other_node)

        self.assertTrue(is_complete(graph))

        graph.unlink_nodes(1,4)

        self.assertFalse(is_complete(graph))

        graph.link_nodes(4,1)

        self.assertTrue(is_complete(graph))

        graph = Graph()

        max = 100
        for i in range (0,max):
            graph.add_node(i)

        for some_node in graph:
            for other_node in graph:
                graph.link_nodes(some_node, other_node)

        self.assertTrue(is_complete(graph))

        graph.del_node(0)

        self.assertTrue(is_complete(graph))

        self.assertEqual(len(graph.get_adjlist(1)), max-2)

        self.assertTrue(graph.is_adjacent(1,max-1))

        with self.assertRaises(TypeError) as context:
            is_complete([])
        self.assertTrue('Incorrect type.' in str(context.exception))

    def test_nodes_by_degree(self):
        graph = Graph()

        self.assertEqual(len(nodes_by_degree(graph)), 0)

        graph.add_node(0)

        self.assertEqual(len(nodes_by_degree(graph)), 1)

        self.assertEqual(nodes_by_degree(graph)[0][1], 0)

        graph.add_node(1)
        graph.link_nodes(0,1)

        self.assertEqual(len(nodes_by_degree(graph)), 2)

        self.assertEqual(nodes_by_degree(graph)[0][1], 1)

        graph = Graph()

        for i in range(0,100):
            graph.add_node(i)

        self.assertEqual(len(nodes_by_degree(graph)), 100)

        for i in range (0,49):
            graph.link_nodes(i, 2*1)
            graph.link_nodes(i, i+1)
            graph.link_nodes(2*1, i-1)

        self.assertTrue(nodes_by_degree(graph)[0][1] > nodes_by_degree(graph)[50][1])
        self.assertFalse(nodes_by_degree(graph)[0][1] < nodes_by_degree(graph)[1][1])

        with self.assertRaises(TypeError) as context:
            nodes_by_degree([])
        self.assertTrue('Incorrect type.' in str(context.exception))


unittest.main()
