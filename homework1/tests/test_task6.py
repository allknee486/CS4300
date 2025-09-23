from task6 import read_text_file
import pytest

def test_task_six():
    file = open("/home/student/CS4300/homework1/task6_read_me.txt")
    word_count = read_text_file()
    assert word_count == 104
    file.close()