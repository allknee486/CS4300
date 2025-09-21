from task3 import printPrimes, sum1to100, checkPosNeg
import pytest

def test_task_three(capsys):
    assert checkPosNeg(5) == 'Positive'
    assert checkPosNeg(-123213) == 'Negative'
    printPrimes()
    captured = capsys.readouterr()
    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"
    assert sum1to100() == 5050 