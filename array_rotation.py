def rotate_array_left(arr, positions):
    """
    Rotate an array of integers to the left by a specified number of positions.
    
    Args:
        arr (list): Array of integers to rotate
        positions (int): Number of positions to rotate left (must be non-negative)
    
    Returns:
        list: Rotated array
        
    Raises:
        ValueError: If positions is negative
        TypeError: If arr is not a list or positions is not an integer
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(positions, int):
        raise TypeError("Positions must be an integer")
    
    if positions < 0:
        raise ValueError("Positions must be non-negative")
    
    # Handle empty array
    if not arr:
        return arr
    
    # Handle case where positions is greater than array length
    # We only need to rotate by the remainder
    n = len(arr)
    effective_positions = positions % n
    
    # If no rotation needed, return original array
    if effective_positions == 0:
        return arr.copy()
    
    # Perform the rotation
    rotated = arr[effective_positions:] + arr[:effective_positions]
    return rotated


def main():
    """Test the array rotation function with various examples."""
    
    # Test cases
    test_cases = [
        # (array, positions, expected_result, description)
        ([1, 2, 3, 4, 5, 6, 7], 2, [3, 4, 5, 6, 7, 1, 2], "Basic rotation by 2"),
        ([1, 2, 3, 4, 5, 6, 7], 8, [2, 3, 4, 5, 6, 7, 1], "Rotation by 8 (greater than array length)"),
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7], "No rotation"),
        ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7], "Full rotation"),
        ([1, 2, 3], 1, [2, 3, 1], "Small array rotation"),
        ([], 3, [], "Empty array"),
        ([1], 5, [1], "Single element array"),
    ]
    
    print("Testing Array Rotation Function")
    print("=" * 40)
    
    for i, (arr, positions, expected, description) in enumerate(test_cases, 1):
        try:
            result = rotate_array_left(arr, positions)
            success = result == expected
            status = "✓ PASS" if success else "✗ FAIL"
            
            print(f"Test {i}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Expected: {expected}")
            print(f"  Result: {result}")
            print(f"  Status: {status}")
            print()
            
        except Exception as e:
            print(f"Test {i}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Error: {e}")
            print()
    
    # Test error cases
    print("Testing Error Cases")
    print("=" * 40)
    
    error_cases = [
        # (array, positions, expected_error, description)
        ([1, 2, 3], -1, ValueError, "Negative positions"),
        ([1, 2, 3], 1.5, TypeError, "Float positions"),
        ("not a list", 2, TypeError, "String instead of list"),
    ]
    
    for i, (arr, positions, expected_error, description) in enumerate(error_cases, 1):
        try:
            result = rotate_array_left(arr, positions)
            print(f"Error Test {i}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Result: {result}")
            print(f"  Status: ✗ FAIL (should have raised {expected_error.__name__})")
            print()
        except Exception as e:
            is_correct_error = isinstance(e, expected_error)
            status = "✓ PASS" if is_correct_error else "✗ FAIL"
            print(f"Error Test {i}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Error: {e}")
            print(f"  Status: {status}")
            print()


if __name__ == "__main__":
    main() 