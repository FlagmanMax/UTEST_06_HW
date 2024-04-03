"""
Unit-tests using pytest
"""
from io import StringIO
import pytest

from task_01_class import ClassMethods
import task_01


@pytest.mark.parametrize("test_list, expected", [
    ([1, 2, 3], 2),
    ([-1, -2, 3], 0),
    ([0, 0, 0], 0)])
def test_get_average_for_list(test_list, expected):
    """
    Parametrizes positive test case for function get_average_for_list()
    :param test_list:
    :param expected:
    :return:
    """
    assert ClassMethods.get_average_for_list(test_list) == expected


@pytest.mark.parametrize("error_list, expected", [
    ([], "No value entered!"),
    (1.8, "Not a list entered!")])
def test_get_average_for_blank_list(error_list, expected):
    """
    Parametrized negative test case for function get_average_for_list()
    :param error_list:
    :param expected:
    :return:
    """
    with pytest.raises(TypeError, match=expected):
        ClassMethods.get_average_for_list(error_list)


@pytest.mark.parametrize("test_string, expected_list", [
    ("1 2 3", [1, 2, 3]),
    ("0 0 0", [0, 0, 0])])
def test_input_list(monkeypatch, test_string, expected_list):
    """
    Parametrized positive test case for function input_list()
    :param monkeypatch:
    :param test_string:
    :param expected_list:
    :return:
    """
    monkeypatch.setattr('builtins.input', lambda : test_string)
    assert ClassMethods.input_list() == expected_list


@pytest.mark.parametrize("num, test_string, expected_tuple", [
    (1, "1 2 3", (2, 1)),
    (2, "4 5 6", (5, 2))])
def test_input_list_safe_and_count_average(monkeypatch, num, test_string, expected_tuple):
    """
    Parametrized positive test case for function test_input_list_safe_and_count_average()
    :param monkeypatch:
    :param num:
    :param test_string:
    :param expected_tuple:
    :return:
    """
    monkeypatch.setattr('builtins.input', lambda: test_string)
    assert ClassMethods.input_list_safe_and_count_average(num) == expected_tuple


@pytest.mark.parametrize("test_string, exception_string_embedded, exception_string_method", [
    ("1 2 a", "EOF when reading a line", "% Input error"),
    ("\n", "EOF when reading a line", "% Input error")])
def test_input_list_safe_and_count_average_value_error(capsys,\
                                                       monkeypatch,\
                                                       test_string,\
                                                       exception_string_embedded,
                                                       exception_string_method):
    """
    Parametrized negative test case for function input_list_safe_and_count_average_value()
    :param capsys:
    :param monkeypatch:
    :param num:
    :param test_string:
    :param exception_string_embedded:
    :param exception_string_method:
    :return:
    """
    monkeypatch.setattr('sys.stdin', StringIO(test_string))

    with pytest.raises(Exception, match=exception_string_embedded):
        ClassMethods.input_list_safe_and_count_average(1)

    captured = capsys.readouterr()
    assert exception_string_method.strip() == captured.out.strip()


@pytest.mark.parametrize("test_strings_array, expected_string", [
    (["1 2 3", "1 2 3"],  "% Средние значения равны"),
    (["1 2 3", "4 5 6"],  "% Второй список имеет большее среднее значение"),
    (["4 5 6", "1 2 3"],  "% Первый список имеет большее среднее значение")])
def test_action(capsys,\
                monkeypatch,\
                test_strings_array,\
                expected_string):
    """
    Parametrized positive test case for function test_input_list_safe_and_count_average()
    :param monkeypatch:
    :param test_strings_array:
    :param expected_string:
    :return:
    """
    responses = iter(test_strings_array)
    monkeypatch.setattr('builtins.input', lambda : next(responses))

    # mock_stdout = io.StringIO()
    # monkeypatch.setattr(sys, 'stdout', mock_stdout)

    task_01.action()
    # assert mock_stdout.getvalue().split('\n')[1:1:5] == expected_string
    captured = capsys.readouterr()
    assert expected_string.strip() == captured.out.strip().split("\n")[-1]
