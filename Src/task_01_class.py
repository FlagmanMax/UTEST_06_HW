"""
Functions for getting list and counting average values for it
"""
class ClassMethods:
    """
    Functions combined in a class
    """
    @staticmethod
    def get_average_for_list(some_list):
        """
        Count average value for a given list, check for types of input values
        :param some_list:
        :return:
        """
        if not isinstance(some_list, list):
            raise TypeError("Not a list entered!")
        if not some_list:
            raise TypeError("No value entered!")
        return sum(some_list) / len(some_list)
    @staticmethod
    def input_list():
        """
        Enter values for a list
        :return:
        """
        float_list = []
        for element in input().split():
            float_list.append(float(element))
        return float_list
    @staticmethod
    def input_list_safe_and_count_average(num):
        """
        Enter values for a list, check entered values
        :param num:
        :return:
        """
        while True:
            try:
                float_list = []
                float_list = ClassMethods.input_list()
                float_average = ClassMethods.get_average_for_list(float_list)
                tup = (float_average, num)
                return tup
            except ValueError:
                print("% Input error")
                continue
            except TypeError:
                print("% Input error")
                continue
                