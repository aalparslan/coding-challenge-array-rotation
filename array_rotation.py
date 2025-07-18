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
    
    if type(positions) != int:
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


# Example usage
if __name__ == "__main__":
    # Simple example
    arr = [1, 2, 3, 4, 5, 6, 7]
    positions = 2
    result = rotate_array_left(arr, positions)
    print(f"Original array: {arr}")
    print(f"Rotated {positions} positions left: {result}")
    
    # Example with large rotation
    large_rotation = 8
    result2 = rotate_array_left(arr, large_rotation)
    print(f"Rotated {large_rotation} positions left: {result2}") 