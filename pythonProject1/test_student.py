import pytest
from lab04zad10 import Student

def test_eq_same_index():
    s1 = Student("Anna", "Kowalska", 123456)
    s2 = Student("John", "Doe", 123456)
    assert s1 == s2  # Test sprawdza, czy studenci z tym samym indexem są równi

def test_eq_different_index():
    s1 = Student("Anna", "Kowalska", 123456)
    s2 = Student("John", "Doe", 654321)
    assert s1 != s2  # Test sprawdza, czy studenci z różnymi indeksami nie są równi

def test_eq_type_check():
    s1 = Student("Anna", "Kowalska", 123456)
    assert s1 != 123456  # Test sprawdza, czy porównanie studenta z liczbą zwraca False
