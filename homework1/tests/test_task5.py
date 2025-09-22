from task5 import book_list, create_student_database
import pytest

def test_task_five(capsys):
    books = book_list()
    for book in books[0:3]:
        print(book)
    captured = capsys.readouterr()
    captured = captured.out.strip().split('\n')
    assert len(captured) == 3

    student_data = create_student_database()
    assert type(student_data) == dict