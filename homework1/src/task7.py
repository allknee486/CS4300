import numpy as np

def matrix_operations(a: np.ndarray, b: np.ndarray):
    return {
        "Addition" : a + b,
        "Subtraction" : a - b,
        "Multiplication" : a * b,
        "Transpose" : a.T
    }