"""
Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и
выполняет следующие действия:
a. Рассчитывает среднее значение каждого списка.
b. Сравнивает эти средние значения и выводит соответствующее сообщение:
- ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
- ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
- ""Средние значения равны"", если средние значения списков равны.

Важно:

Приложение должно быть написано в соответствии с принципами
объектно-ориентированного программирования.

Используйте Pytest (для Python) или JUnit (для Java) для написания тестов, которые проверяют
правильность работы программы. Тесты должны учитывать различные сценарии использования
вашего приложения.

Используйте pylint (для Python) или Checkstyle (для Java)
для проверки качества кода.

Сгенерируйте отчет о покрытии кода тестами.
Ваша цель - достичь минимум 90% покрытия.
"""

from task_01_class import ClassMethods

# Constant value; Number of lists; Value in range 2..5
NUMBER_OF_LISTS = 2
ANSWER_LIST = ["Первый ","Второй ", "Третий ", "Четвертый ", "Пятый "]

def action():
    """
    Main action
    :return:
    """
    # Create list of tuples with data: (average value, number of list)
    result = []
    for num in range(NUMBER_OF_LISTS):
        # Create tuple variable
        tup = ()
        print(f"% Enter list {num + 1}: ")
        tup = ClassMethods.input_list_safe_and_count_average(num)
        result.append(tup)
        print(f"% Average value for list {num + 1} = ", tup[0])

    # Sort list of tuples in reverse order
    result.sort(reverse=True)

    # Create answer string variable
    answer = "% "
    if result[0][0] == result[-1][0]:
        answer = "% Средние значения равны"
    else:
        for num in range(NUMBER_OF_LISTS-1):
            if len(answer) != 2:
                answer += "и "
            answer += ANSWER_LIST[result[num][1]]
            if result[num][0] != result[num+1][0]:
                answer += "список имеет большее среднее значение"
                break
    print(answer)

if __name__ == '__main__':
    action()
