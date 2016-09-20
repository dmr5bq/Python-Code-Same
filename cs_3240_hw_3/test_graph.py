import unittest
from graph import Graph

class TestGraphMethods(unittest.TestCase):

    def test_init(self):

        tmp = Graph()
        self.assertEqual(tmp.nodes_dict, {})

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        tmp = Graph(insert_dict)
        self.assertEqual(tmp.nodes_dict, insert_dict)

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        self.assertNotEqual(tmp.nodes_dict, insert_dict)

    def test_get_adjlist(self):

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertEqual(tmp.get_adjlist(1), [2])
        self.assertEqual(tmp.get_adjlist(2), [1])
        self.assertNotEqual(tmp.get_adjlist(1), tmp.get_adjlist(2))
        self.assertIsNone(tmp.get_adjlist(0))

    def test_is_adjacent(self):

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertFalse(tmp.is_adjacent(0,1))
        self.assertFalse(tmp.is_adjacent(1,1))
        self.assertFalse(tmp.is_adjacent(1,3))
        self.assertTrue(tmp.is_adjacent(1,2) and tmp.is_adjacent(2,1))

    def test_num_nodes(self):
        tmp = Graph()

        self.assertEqual(tmp.num_nodes(), 0)

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertEqual(tmp.num_nodes(), 3)

    def test_str(self):

        graph = Graph()

        self.assertEqual(str(graph), str({}))

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertEqual(str(tmp), str(tmp.nodes_dict))

    def test_iter(self):
        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        bool1 = 1 in tmp
        bool2 = 0 in tmp

        self.assertTrue(bool1)
        self.assertFalse(bool2)


    def test_len(self):
        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertEqual(len(tmp), len(tmp.nodes_dict))

        tmp = Graph()

        self.assertEqual(len(tmp), 0)

    def test_add_node(self):

        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertTrue(tmp.add_node(4))
        self.assertFalse(tmp.add_node(3))
        self.assertFalse(tmp.add_node(4))

    def test_link_nodes(self):
        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertTrue(tmp.link_nodes(1,3))
        self.assertFalse(tmp.link_nodes(3,1))
        self.assertFalse(tmp.link_nodes(1,2) and tmp.link_nodes(2,1))

        self.assertTrue(tmp.is_adjacent(1,3) and tmp.is_adjacent(3,1))

        self.assertFalse(tmp.link_nodes(0,1))

    def test_unlink_nodes(self):
        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertTrue(tmp.unlink_nodes(1,2) and not tmp.unlink_nodes(1,2) and tmp.link_nodes(1,2))

        self.assertFalse(tmp.unlink_nodes(0,1))
        self.assertFalse(tmp.unlink_nodes(1,1))

    def test_del_node(self):
        insert_dict = {}
        insert_dict[1] = []
        insert_dict[2] = []
        insert_dict[3] = []

        insert_dict[1] = [2]
        insert_dict[2] = [1]

        tmp = Graph(insert_dict)

        self.assertTrue(tmp.del_node(1) and not tmp.del_node(1))
        self.assertFalse(tmp.del_node(0))
        self.assertFalse(tmp.is_adjacent(1,2))
        self.assertFalse(1 in tmp)




if __name__ == '__main__':
    unittest.main()
