from AlgoToolkit.algo import bubble_sort
from AlgoToolkit.algo import binary_search
from AlgoToolkit.algo import dijkstra

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1

def test_dijkstra():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3},
        'D': {'B': 10, 'C': 3}
    }

    distances, previous = dijkstra(graph, 'A')

    assert distances == {'A': 0, 'B': 4, 'C': 2, 'D': 5}
    assert previous == {'A': None, 'B': 'A', 'C': 'A', 'D': 'C'}    