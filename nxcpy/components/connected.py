# -*- coding: utf-8 -*-
"""
Connected components.
"""

import networkx as nx
from networkx.utils.decorators import not_implemented_for
import nxcpy as nxc
from nxc.components import _connected

__all__ = [
        'connected_components',
        'is_connected'
]

@not_implemented_for('directed')
def is_connected(G):
    """Return True if the graph is connected, false otherwise.

    Parameters
    ----------
    G : NetworkX Graph
       An undirected graph.

    Returns
    -------
    connected : bool
      True if the graph is connected, false otherwise.

    Examples
    --------
    >>> G = nx.path_graph(10)
    >>> print(nxc.is_connected(G))
    True

    See Also
    --------
    connected_components

    Notes
    -----
    For undirected graphs only.

    """
    connected = _connected.is_connected(G.adjacency_iter())
    return True if connected else False

@not_implemented_for('directed')
def connected_components(G):
    """Return the number of connected components in a graph.

    Parameters
    ----------
    G : NetworkX Graph
       An undirected graph

    Returns
    -------
    comp = generator of sets
      A generator of nodes of each component of G

    Examples
    --------
    >>> G = nx.path_graph(10)
    >>> G.add_path([10, 11, 12])
    >>> list(nxc.connected_components(G))
    [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), set([10, 11, 12])]

    Notes
    -----
    For undirected graphs only.

    """
    components = _connected.connected_components(G.adjacency_iter())
    return components


