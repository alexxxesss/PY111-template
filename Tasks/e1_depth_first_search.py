from typing import Hashable, List
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
            )

    plt.show()


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    draw_graph(g)

    path_nodes = []  # полностью сгоревшие узлы
    visit_nodes = {node: False for node in g.nodes}  # посещенные узлы

    wait_nodes = []  # стек
    wait_nodes.append(start_node)  # добавляем в стек / вершина справа
    visit_nodes[start_node] = True  # при добавлении узла в очередь он считается посещенным

    while wait_nodes:  # пока есть горящие узлы (очередь не пустая) будем зажигать :)
        current_node = wait_nodes.pop()  # забираем горящий узел с конца очереди
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visit_nodes[neighbour]:
                wait_nodes.append(neighbour)
                visit_nodes[neighbour] = True

        path_nodes.append(current_node)  # полностью сожгли

    return path_nodes
