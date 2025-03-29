# AlgoToolkit

**A Python package for sorting and searching algorithms.**

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
You can install the package using `pip` after building it or directly from source:

```bash
git clone https://github.com/alok1304/AlgoToolkit.git
cd AlgoToolkit
pip install .
```

## 🚀 Usage
```python
from AlgoToolkit.algo import bubble_sort, binary_search

# Sorting Example
arr = [5, 2, 9, 1]
sorted_arr = bubble_sort(arr)
print("Sorted Array:", sorted_arr)

# Searching Example
target = 2
index = binary_search(sorted_arr, target)
print(f"Element found at index {index}")

# Example using shell
>>> from AlgoToolkit import algo
>>> algo.bubble_sort([3,7,1,2,5])
[1, 2, 3, 5, 7]
>>> algo.binary_search([1,3,5,7,9],7)
3
```

## 🧪 Running Tests
Ensure you have `pytest` installed:

```bash
pip install pytest
pytest tests/
```

## 📦 Project Structure
```plaintext
AlgoToolkit/
├── AlgoToolkit/
│   ├── __init__.py
│   └── algo.py
├── tests/
│   └── test_algo.py
├── pyproject.toml
├── README.md
├── LICENSE
├── requirements.txt
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request with your changes.

## 🌟 Author
Developed by **Alok Kumar**.

