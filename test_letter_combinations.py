"""Unit tests for letter_combinations.py, AAA pattern"""

import pytest
from letter_combinations import letter_combinations

class TestLetterCombinations:
    def test_empty_input(self):
        
        digits = ""
        
        result = letter_combinations(digits)
        
        assert result == []
    def test_two_digit(self):

        digits = "23"
        expected_output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        
        result = letter_combinations(digits)
        
        assert sorted(result) == sorted(expected_output)
    def test_three_digit(self):
        
        digits = "234"
        expected_count = 27
        
        result = letter_combinations(digits)
        
        assert len(result) == expected_count
    def test_invalid_digit(self):
        digits = "1"
        
        result = letter_combinations(digits)
        
        assert result == []
    def test_multiple_invalid_digits(self):
        digits = "1a9"
        
        result = letter_combinations(digits)
        
        assert result == []

    def test_mixed_valid_invalid_digits(self):
        digits = "2a3"
        
        result = letter_combinations(digits)
        
        assert result == []
    def test_repeated_digits(self):
        digits = "222"
        expected_count = 27
        
        result = letter_combinations(digits)
        
        assert len(result) == expected_count
    def test_max_input(self):
        digits = "2345"
        expected_count = 81
        
        result = letter_combinations(digits)
        
        assert len(result) == expected_count
    def test_longer_than_4_input(self):
        digits = "23456"
        
        result = letter_combinations(digits)
        
        assert result == []

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
