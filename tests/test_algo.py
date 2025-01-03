from AlgoToolkit.algo import bubble_sort,binary_search

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1