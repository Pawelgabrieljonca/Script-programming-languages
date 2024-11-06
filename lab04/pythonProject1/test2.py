import pytest
from zadanie11 import  student_grades


# Testy dla funkcji student_grades
def test_student_grades_basic():
    results = student_grades()
    assert results[0]["średnia_ocen"] == 4.2
    assert results[1]["średnia_ocen"] == 3.8
    assert results[2]["średnia_ocen"] == 4.4

def test_student_grades_correct_data():
    results = student_grades()
    assert results[0]["imię"] == "Paweł"
    assert results[1]["nazwisko"] == "Nowak"
    assert results[2]["numer_indeksu"] == 12345

def test_student_grades_data_structure():
    results = student_grades()
    assert isinstance(results, list)
    assert isinstance(results[0], dict)
    assert "średnia_ocen" in results[0]