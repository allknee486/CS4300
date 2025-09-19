from task1 import hello_world
import pytest

def test_task1(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"