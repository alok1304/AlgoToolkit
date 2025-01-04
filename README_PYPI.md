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
```

##  Expected Output:
- For Bubble Sort:
```bash
Sorted array using Bubble Sort: [1, 2, 5, 5, 6, 9]
````
- For Binary Search:
```bash
Index of 5 using Binary Search: 2
```

