from task2 import test_bool, test_float, test_int, test_string
import pytest

def test_task2():
    assert type(test_int) == int
    assert type(test_float) == float 
    assert type(test_string) == str
    assert type(test_bool) == bool 