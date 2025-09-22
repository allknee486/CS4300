from task5 import book_list
import pytest

def test_task_five(capsys):
    books = book_list()
    for book in books[0:3]:
        print(book)
    captured = capsys.readouterr()
    captured = captured.out.strip().split('\n')
    assert len(captured) == 3