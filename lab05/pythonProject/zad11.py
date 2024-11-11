import pytest
import math
# Test 1: Sprawdzamy liczbę całkowitą
def test_trunc_integer():
    assert math.trunc(5) == 5, "Test nie przeszedł! Oczekiwano 5."

# Test 2: Sprawdzamy liczbę zmiennoprzecinkową
def test_trunc_float():
    assert math.trunc(5.67) == 5, "Test nie przeszedł! Oczekiwano 5."

# Test 3: Sprawdzamy liczbę ujemną
def test_trunc_negative():
    assert math.trunc(-5.67) == -5, "Test nie przeszedł! Oczekiwano -5."
