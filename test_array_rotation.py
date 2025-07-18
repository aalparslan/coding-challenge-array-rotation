#!/usr/bin/env python3
"""
Comprehensive test suite for array rotation functionality.
"""

import time
from array_rotation import rotate_array_left


def test_functional_cases():
    """Test all functional cases for array rotation."""
    
    test_cases = [
        # (array, positions, expected_result, description)
        ([1, 2, 3, 4, 5, 6, 7], 2, [3, 4, 5, 6, 7, 1, 2], "Basic rotation by 2"),
        ([1, 2, 3, 4, 5, 6, 7], 8, [2, 3, 4, 5, 6, 7, 1], "Rotation by 8 (greater than array length)"),
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7], "No rotation"),
        ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7], "Full rotation"),
        ([1, 2, 3], 1, [2, 3, 1], "Small array rotation"),
        ([], 3, [], "Empty array"),
        ([1], 5, [1], "Single element array"),
        
        # Additional edge cases
        ([1, 2, 3, 4, 5, 6, 7], 14, [1, 2, 3, 4, 5, 6, 7], "Double full rotation (14 positions)"),
        ([1, 2, 3, 4, 5, 6, 7], 21, [1, 2, 3, 4, 5, 6, 7], "Triple full rotation (21 positions)"),
        ([1, 2, 3, 4, 5, 6, 7], 1, [2, 3, 4, 5, 6, 7, 1], "Single position rotation"),
        ([1, 2, 3, 4, 5, 6, 7], 6, [7, 1, 2, 3, 4, 5, 6], "Almost full rotation (6 positions)"),
        ([1, 2, 3, 4, 5, 6, 7], 13, [7, 1, 2, 3, 4, 5, 6], "Full rotation + 6 positions"),
        
        # Edge cases with different array sizes
        ([1, 2], 1, [2, 1], "Two element array rotation"),
        ([1, 2], 3, [2, 1], "Two element array with large rotation"),
        ([1, 2, 3, 4], 2, [3, 4, 1, 2], "Four element array rotation"),
        ([1, 2, 3, 4], 6, [3, 4, 1, 2], "Four element array with large rotation"),
        
        # Large arrays
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [4, 5, 6, 7, 8, 9, 10, 1, 2, 3], "Large array rotation"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23, [4, 5, 6, 7, 8, 9, 10, 1, 2, 3], "Large array with large rotation"),
        
        # Arrays with repeated elements
        ([1, 1, 1, 2, 2, 2], 2, [1, 2, 2, 2, 1, 1], "Array with repeated elements"),
        ([0, 0, 0, 0], 1, [0, 0, 0, 0], "Array with all zeros"),
        ([1, 1, 1, 1], 3, [1, 1, 1, 1], "Array with all ones"),
        
        # Negative numbers and mixed types
        ([-1, -2, -3, -4], 2, [-3, -4, -1, -2], "Array with negative numbers"),
        ([1, -1, 2, -2], 1, [-1, 2, -2, 1], "Array with mixed positive/negative"),
        
        # Very large rotation amounts
        ([1, 2, 3, 4, 5], 1000, [1, 2, 3, 4, 5], "Very large rotation amount (1000)"),
        ([1, 2, 3, 4, 5], 1001, [2, 3, 4, 5, 1], "Very large rotation amount (1001)"),
        
        # Edge cases with modulo behavior
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5], "Rotation equal to array length"),
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5], "Rotation equal to twice array length"),
        ([1, 2, 3, 4, 5], 15, [1, 2, 3, 4, 5], "Rotation equal to thrice array length"),
    ]
    
    print("Testing Array Rotation Function")
    print("=" * 40)
    
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, (arr, positions, expected, description) in enumerate(test_cases, 1):
        try:
            result = rotate_array_left(arr, positions)
            success = result == expected
            status = "✓ PASS" if success else "✗ FAIL"
            if success:
                passed_tests += 1
            
            print(f"Test {i:2d}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Expected: {expected}")
            print(f"  Result: {result}")
            print(f"  Status: {status}")
            print()
            
        except Exception as e:
            print(f"Test {i:2d}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Error: {e}")
            print()
    
    print(f"Test Summary: {passed_tests}/{total_tests} tests passed")
    print("=" * 40)
    return passed_tests, total_tests


def test_error_cases():
    """Test error handling cases."""
    
    error_cases = [
        # (array, positions, expected_error, description)
        ([1, 2, 3], -1, ValueError, "Negative positions"),
        ([1, 2, 3], -5, ValueError, "Large negative positions"),
        ([1, 2, 3], 1.5, TypeError, "Float positions"),
        ([1, 2, 3], 2.0, TypeError, "Float positions (whole number)"),
        ("not a list", 2, TypeError, "String instead of list"),
        (None, 2, TypeError, "None instead of list"),
        ([1, 2, 3], "2", TypeError, "String positions"),
        ([1, 2, 3], None, TypeError, "None positions"),
        ([1, 2, 3], True, TypeError, "Boolean positions"),
        ([1, 2, 3], False, TypeError, "Boolean positions (False)"),
        ([1, 2, 3], [], TypeError, "List positions"),
        ([1, 2, 3], {}, TypeError, "Dict positions"),
        ([1, 2, 3], (), TypeError, "Tuple positions"),
    ]
    
    print("Testing Error Cases")
    print("=" * 40)
    
    passed_error_tests = 0
    total_error_tests = len(error_cases)
    
    for i, (arr, positions, expected_error, description) in enumerate(error_cases, 1):
        try:
            result = rotate_array_left(arr, positions)
            print(f"Error Test {i:2d}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Result: {result}")
            print(f"  Status: ✗ FAIL (should have raised {expected_error.__name__})")
            print()
        except Exception as e:
            is_correct_error = isinstance(e, expected_error)
            status = "✓ PASS" if is_correct_error else "✗ FAIL"
            if is_correct_error:
                passed_error_tests += 1
            print(f"Error Test {i:2d}: {description}")
            print(f"  Input: {arr}, rotate {positions} positions left")
            print(f"  Error: {e}")
            print(f"  Status: {status}")
            print()
    
    print(f"Error Test Summary: {passed_error_tests}/{total_error_tests} error tests passed")
    print("=" * 40)
    return passed_error_tests, total_error_tests


def test_performance():
    """Test performance with large arrays and rotations."""
    
    print("Performance Test")
    print("=" * 40)
    
    # Test with large array and large rotation
    large_array = list(range(1000))
    large_rotation = 999999
    
    start_time = time.time()
    result = rotate_array_left(large_array, large_rotation)
    end_time = time.time()
    
    expected_large = list(range(999, 1000)) + list(range(999))
    success = result == expected_large
    
    print(f"Large array test (1000 elements, 999999 rotations):")
    print(f"  Time taken: {(end_time - start_time)*1000:.2f} ms")
    print(f"  Status: {'✓ PASS' if success else '✗ FAIL'}")
    print(f"  Result correct: {success}")
    print()
    
    return success


def run_all_tests():
    """Run all test suites."""
    
    print("🧪 ARRAY ROTATION TEST SUITE")
    print("=" * 50)
    print()
    
    # Run functional tests
    func_passed, func_total = test_functional_cases()
    
    # Run error tests
    error_passed, error_total = test_error_cases()
    
    # Run performance test
    perf_success = test_performance()
    
    # Summary
    print("=" * 50)
    print("📊 FINAL TEST SUMMARY")
    print("=" * 50)
    print(f"Functional Tests: {func_passed}/{func_total} passed")
    print(f"Error Tests: {error_passed}/{error_total} passed")
    print(f"Performance Test: {'✓ PASS' if perf_success else '✗ FAIL'}")
    
    total_passed = func_passed + error_passed + (1 if perf_success else 0)
    total_tests = func_total + error_total + 1
    
    print(f"\nOverall: {total_passed}/{total_tests} tests passed")
    
    if total_passed == total_tests:
        print("🎉 ALL TESTS PASSED!")
    else:
        print("❌ Some tests failed!")
    
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests() 