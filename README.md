# 🌀 Palindrome Decision Algorithms

This repository contains different implementations of algorithms to determine whether a given string is a **palindrome**. The methods vary in approach and efficiency, from using pointers to recursion.


## 🚀 Technologies Used
- **Python 3.12**
- **Pandas** (for data handling)
- **Matplotlib** (for visualization)
- **Unittest** (for testing)
- **Coverage.py** (for coverage analysis)

---

## ⚡ Implemented Algorithms

- **🔄 Reverse Method (`isPalindromeReverse`)**  
  Checks if a string is a palindrome by reversing it and comparing it to the original.  
  📌 **Time Complexity:** _O(n)_

- **🎯 Two-Pointer Method (`isPalindromePointers`)**  
  Uses two pointers, one at the beginning and one at the end, comparing characters while moving towards the center.  
  📌 **Time Complexity:** _O(n)_

- **🔁 Recursive Method (`isPalindromeRecursive`)**  
  Recursively checks if a string is a palindrome by comparing the first and last characters and calling itself on the substring in between.  
  📌 **Time Complexity:** _O(n)_



## 🛠 How to Use

## ✅ Run tests with coverage

```sh
coverage run -m unittest discover -s tests
```

## 📊 Generate coverage report:
```sh
coverage report -m
```

##  Executing the Main Script
```sh
python main.py
```
