from task4 import calculate_discount
import pytest

def test_task_four():
    assert calculate_discount(100, 10) == 10
    assert calculate_discount(99.122, 10) == 9.9122
    assert calculate_discount(123231121312.9123213, 100) == 123231121312.9123213