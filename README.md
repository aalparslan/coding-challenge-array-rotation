# Array Rotation Solution

This repository contains a Python solution for rotating arrays of integers to the left by a specified number of positions.

## Problem Description

The problem involves rotating an array of integers to the left by a specified number of positions. The solution handles various edge cases including:

- Basic rotation (e.g., `[1,2,3,4,5,6,7]` rotated 2 positions left becomes `[3,4,5,6,7,1,2]`)
- Rotation amounts greater than array length (e.g., rotating 8 positions in a 7-element array)
- Negative position values (throws error)
- Empty arrays and single-element arrays

## Solution Features

- **Efficient Algorithm**: Uses slicing for O(1) time complexity
- **Edge Case Handling**: Handles rotation amounts greater than array length using modulo operation
- **Input Validation**: Validates input types and handles negative values gracefully
- **Comprehensive Testing**: Includes test cases for all scenarios

## Usage

```python
from array_rotation import rotate_array_left

# Basic usage
arr = [1, 2, 3, 4, 5, 6, 7]
result = rotate_array_left(arr, 2)
# result: [3, 4, 5, 6, 7, 1, 2]

# Handle large rotation amounts
result = rotate_array_left(arr, 8)
# result: [2, 3, 4, 5, 6, 7, 1]
```

## Running Tests

```bash
python3 array_rotation.py
```

## Requirements

- Python 3.x

## Branch Information

- **Branch**: `array-rotation-solution`
- **Commit**: Initial implementation with comprehensive testing 