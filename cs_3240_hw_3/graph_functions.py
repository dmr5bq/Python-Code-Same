from graph import Graph


def is_complete(graph):
    if isinstance(graph, Graph):
        graph_node_count = graph.num_nodes()

        if len(graph) is 0 or len(graph) is 1:
            return True

        for some_node in graph:
            list_node_count = len(graph.nodes_dict[some_node])
            if list_node_count != (graph_node_count - 1):
                return False
        return True
    else:
        raise TypeError('Incorrect type.')


def nodes_by_degree(graph):

    ret_list = []
    if isinstance(graph, Graph):
        for some_node in graph:
            tuple_to_store = (some_node, len(graph.get_adjlist(some_node)))
            ret_list.append(tuple_to_store)

        ret_list.sort(key=lambda degree:degree[1], reverse=True)
        return ret_list
    else:
        raise TypeError('Incorrect type.')
