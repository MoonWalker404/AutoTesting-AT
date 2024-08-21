# AutoTesting-AT/test_main.py
import pytest
from main import count_vowels

def test_vowels_only():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfgBCDFG") == 0

def test_mixed_case():
    assert count_vowels("Hello World!") == 3
    assert count_vowels("PYTHON") == 1

if __name__ == "__main__":
    pytest.main()
