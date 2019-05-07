def string_calculator():
    def string_should_return_0_for_empty_string():
        assert add("") == 0

    def string_will_return_input_as_output_for_single_numbers():
        assert add("3") == 3
        assert add("8") == 8

    def string_will_return_sum_of_multiple_numbers_serarated_by_commas():
        assert add("2,5") == 7
        assert add("1,3,6") == 10

    def string_will_add_numbers_in_new_lines_between_numbers():
        assert add("1\n2,3") == 6
        assert add("2\n4") == 6

    def string_will_support_different_delimiters():
        assert add("//;\n1;2") == 3
        assert add("//+\n1+4") == 5

    def string_with_negatives_will_raise_an_exception_error():
        assert raises(ValueError, add, "-7")
        assert raises(ValueError, add, "3, -8")