# AlgoToolkit

A Python package for sorting and searching algorithms.

## 📦 Features
- **Sorting Algorithms:** 
     - Bubble Sort 
     - Merge Sort 
     - Selection Sort 
     - Quick Sort 
     - Insertion Sort
- **Searching Algorithms:** 
     - Binary Search
     - Linear Search
- **Dijkstra's Algorithm:**
  - Finding the shortest path      

## 📚 Installation
You can install the package directly from PyPI:

```bash
pip install algotoolkit
```

## 🚀 Usage
```python
from AlgoToolkit import algo

# Test the bubble sort function
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = algo.bubble_sort(arr)
print(f"Sorted array using Bubble Sort: {sorted_arr}")

# Test the binary search function
sorted_arr = [1, 2, 5, 5, 6, 9]
target = 5
index = algo.binary_search(sorted_arr, target)
print(f"Index of {target} using Binary Search: {index}")

# Test the shortest path using Dijkstra Algorithm
graph = {
     'A': {'B': 4, 'C': 2},
     'B': {'A': 4, 'C': 5, 'D': 10},
     'C': {'A': 2, 'B': 5, 'D': 3},
     'D': {'B': 10, 'C': 3}
}
distances, previous = algo.dijkstra(graph, 'A')
print(distances)
print(previous)
```

##  Expected Output:
- For Bubble Sort:
```bash
Sorted array using Bubble Sort: [1, 2, 5, 5, 6, 9]
```
- For Binary Search:
```bash
Index of 5 using Binary Search: 2
```
- For Shortest Path:
```bash
{'A': 0, 'B': 4, 'C': 2, 'D': 5}
{'A': None, 'B': 'A', 'C': 'A', 'D': 'C'}
```

