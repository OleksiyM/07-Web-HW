from datetime import datetime, timedelta
from random import randint

from faker import Faker

from constants import groups, subjects, professors, students_in_a_group_count, MIN_GRADE, MAX_GRADE, DAYS_DELTA
from db import session
from models import Group, Professor, Subject, Student, Grade


def insert_test_data_into_tables():
    f = Faker()

    for group in groups:
        new_group = Group(name=group)
        session.add(new_group)

    for professor in professors:
        new_professor = Professor(name=professor)
        session.add(new_professor)

    for subject in subjects:
        new_subject = Subject(name=subject, professor_id=randint(1, len(professors)))
        session.add(new_subject)

    for gr_id in range(1, len(groups) + 1):
        for i in range(students_in_a_group_count):
            new_student = Student(name=f.name(), group_id=gr_id)
            session.add(new_student)

    for grade in range(10, randint(11, 20)):
        random_grade = randint(MIN_GRADE, MAX_GRADE)
        random_student_id = randint(1, len(groups) * students_in_a_group_count)
        random_subject_id = randint(1, len(subjects))
        random_date = (datetime.now() - timedelta(days=randint(1, DAYS_DELTA))).date()
        new_grade = Grade(grade=random_grade, student_id=random_student_id, subject_id=random_subject_id,
                          date=random_date)
        session.add(new_grade)


def main():
    try:
        insert_test_data_into_tables()
        session.commit()
        print('Test data were inserted into tables')
    except Exception as e:
        print(f'Error:  {e}')
        session.rollback()
    finally:
        session.close()
        exit(1)


def main_debug():
    insert_test_data_into_tables()
    session.commit()
    print('Test data were inserted into tables')
    session.close()


if __name__ == '__main__':
    main()
