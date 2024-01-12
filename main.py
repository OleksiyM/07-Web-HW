import datetime
from decimal import Decimal

from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, \
    select_10, select_11, select_12

from sqlalchemy import func, desc, and_

from db import session
from models import Grade, Professor, Student, Group, Subject


def get_sql_task_description(task_number: int) -> str:
    messages = (
        'Find 5 students with the highest average score in all subjects.',
        'Find the student with the highest grade point average in a particular subject.',
        'Find the average score in groups for a particular subject.',
        'Find the average grade point average in a stream (across the entire grade table).',
        'Find what courses a certain teacher teaches.',
        'Find a list of students in a particular group.',
        'Find the grades of students in a particular group in a particular subject.',
        'Find the average grade given by a certain teacher in his/her subjects.',
        'Find the list of courses a student is taking.',
        'Find the list of courses taught by a certain teacher to a certain student.',
        'Bonus: The average grade that a certain teacher gives to a certain student.',
        'Bonus: Grades of students in a certain group in a certain subject in the last class.'
    )
    return messages[task_number]


def run_all_queries():
    print('Executing queries...')
    for num in range(1, 13):
        print(f'Query {num}: {get_sql_task_description(num - 1)}')
        print('Result:')
        # print(f'{eval(f"select_{num}")()}')
        func_name = f'select_{num}()'
        print('-' * 85)
        print(list_to_string_formatted(eval(func_name)))
        print('-' * 85)


def list_to_string_formatted(list_of_tuples, date_index=None):
    formatted_string = ''
    for tuple_item in list_of_tuples:
        formatted_tuple = list(tuple_item)
        for i, element in enumerate(formatted_tuple):
            if isinstance(element, datetime.date):
                if date_index is None or i == date_index:
                    formatted_tuple[i] = element.strftime("%Y.%m.%d")
            elif isinstance(element, Decimal):
                formatted_tuple[i] = f"{element:.2f}"  # Format Decimal as string with 2 decimal places
        formatted_string += str(formatted_tuple) + "\n"  # Append formatted tuple to string
    return formatted_string.rstrip()  # Remove trailing newline


if __name__ == '__main__':
    run_all_queries()

    # print(select_12())
    # session.close()
    # exit(0)
