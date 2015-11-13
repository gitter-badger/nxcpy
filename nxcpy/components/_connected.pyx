from libc.stdlib import malloc, free
cimport _api.connected

import networkx as nx

__all__ = [
        'connected_components',
        'is_connected'
]

cdef enum Color:
    WHITE = 0
    GRAY = 1
    BLACK = 2

cdef struct list_node:
    int node
    list_node *next

cdef struct adjacency_list:
    int p  # parent
    int d  # distance
    Color color  # _api.connected.color is an enum
    list_node *next  # The pointer to the list of adjacenct nodes

cdef create_adjacency_list(adj_iter):
    cdef adjacency_list *adj_list


def is_connected(adj_iter):
    adj_list = create_adjacency_list(adj_iter)

