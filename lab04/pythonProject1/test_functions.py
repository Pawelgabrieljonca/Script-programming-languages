import pytest
from zadanie6 import  unique_list


# Testy dla funkcji unique_list
def test_unique_list_basic():
    assert unique_list([1, 2, 3, 4, 3]) == {1, 2, 3, 4}

def test_unique_list_no_duplicates():
    assert unique_list([1, 2, 3, 4]) == {1, 2, 3, 4}

def test_unique_list_empty():
    assert unique_list([]) == set()
