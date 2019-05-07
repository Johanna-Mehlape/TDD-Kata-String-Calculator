import pytest
from string_calculator import *

class test_StringCalculator(object):
    
    def test_add__empty_string_returns_0():
        result = add("")
        assert result == 0

    def test_string_will_return_input_as_output_for_single_numbers():
        result = add("3")
        assert result == 3

        result = add("8")
        assert result == 8

    def test_string_will_return_sum_of_multiple_numbers_serarated_by_commas():
        result = add("2,5")
        assert result == 7

        result = add("1,3,6")
        assert result == 10

    def test_string_will_add_numbers_in_new_lines_between_numbers():
        result = add("1\n2,3")
        assert result == 6
       

