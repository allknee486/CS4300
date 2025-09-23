from task7 import matrix_operations
import pytest
import numpy as np

def test_task_seven():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])

    results =  matrix_operations(a, b)
    expected_add = np.array([[6, 8], [10, 12]])
    assert np.array_equal(expected_add, results["Addition"]) == True

    expected_subtract = np.array([[-4, -4], [-4, -4]])
    assert np.array_equal(expected_subtract, results["Subtraction"]) == True

    expected_multiply = np.array([[5, 12], [21, 32]])
    assert np.array_equal(expected_multiply, results["Multiplication"]) == True

    expected_transpose = np.array([[1, 3], [2, 4]])
    assert np.array_equal(expected_transpose, results["Transpose"]) == True