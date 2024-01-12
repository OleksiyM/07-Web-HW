from sqlalchemy import func, desc, and_

from db import session
from models import Grade, Professor, Student, Group, Subject


def select_1():
    """
    SELECT students.name,
           ROUND(AVG(grades.grade),2) AS average_grade
    FROM students
    JOIN grades ON students.id = grades.student_id
    GROUP BY students.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Grade, Student.id == Grade.student_id).group_by(Student.id).order_by(desc('average_grade')) \
        .limit(5).all()
    return result


def select_2():
    """
    SELECT students.name,
           subjects.name AS subject_name,
           ROUND(AVG(grades.grade),2) AS average_grade
    FROM students JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = 'chemistry'
    GROUP BY students.id, subjects.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.name, Subject.name.label('subject_name'),
                           func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == 'chemistry').group_by(Student.id, Subject.id).order_by(desc('average_grade')) \
        .limit(1).all()
    return result


def select_3():
    """
    SELECT groups.name AS group_name,
           round(AVG(grades.grade),2) AS average_grade
    FROM groups
    JOIN students ON groups.id = students.group_id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE subjects.name = 'chemistry'
    GROUP BY groups.id, groups.name
    ORDER BY average_grade DESC;
    """
    result = session.query(Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Student, Group.id == Student.group_id).join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id).filter(Subject.name == 'chemistry').group_by(Group.id,
                                                                                                    Group.name) \
        .order_by(desc('average_grade')).all()
    return result


def select_4():
    """
    SELECT ROUND(AVG(grades.grade),2) AS average_grade
    FROM grades;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')).all()
    return result


def select_5():
    """
    SELECT p.name as professor_name,
    s.name as subject
    FROM professors p
    JOIN subjects s ON p.id = s.professor_id
    WHERE p.id =3;
    """
    result = session.query(Professor.name.label('professor_name'), Subject.name.label('subject')).join(Subject,
                                                                                                       Professor.id == Subject.professor_id) \
        .filter(Professor.id == 3).all()
    return result


def select_6():
    """
    SELECT s.name as student_name
    FROM students s
    WHERE group_id = 3
    ORDER BY s.name
    """
    result = session.query(Student.name.label('student_name')).filter(Student.group_id == 3).order_by(
        Student.name).all()
    return result


def select_7():
    """
    SELECT students.group_id as group_number,
           students.name as student_name,
           grades.grade as grade,
           grades.date as date,
           subjects.name as subject
    FROM grades
    JOIN students ON grades.student_id = students.id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE students.group_id = 1
          AND subjects.id = 1
    ORDER BY students.name, grades.date;
    """
    result = session.query(Student.group_id.label('group_number'), Student.name.label('student_name'),
                           Grade.grade.label('grade'), Grade.date.label('date'), Subject.name.label('subject')) \
        .join(Student, Grade.student_id == Student.id).join(Subject, Grade.subject_id == Subject.id) \
        .filter(and_(Student.group_id == 1, Subject.id == 1)).order_by(Student.name, Grade.date).all()

    return result


def select_8():
    """
    SELECT p.name as professor_name,
    ROUND(AVG(g.grade),2) as average_grade
    FROM professors p
    JOIN subjects s ON p.id = s.professor_id
    JOIN grades g ON g.subject_id = s.id
    WHERE p.id = 1
    GROUP BY p.id
    """
    result = session.query(Professor.name.label('professor_name'),
                           func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Subject, Professor.id == Subject.professor_id).join(Grade, Subject.id == Grade.subject_id) \
        .filter(Professor.id == 1).group_by(Professor.id).all()
    return result


def select_9():
    """
    SELECT DISTINCT subjects.name AS subject,
    students.name AS student_name
    FROM students
    JOIN grades g ON students.id = g.student_id
    JOIN subjects ON g.subject_id =  subjects.id
    WHERE students.id = 1
    """
    result = session.query(Subject.name.label('subject'), Student.name.label('student_name')) \
        .join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id) \
        .filter(Student.id == 1).distinct().all()
    return result


def select_10():
    """
    SELECT DISTINCT subjects.name AS subject,
    students.name AS student_name,
    p.name AS professor_name
    FROM students
    JOIN grades g ON students.id = g.student_id
    JOIN subjects ON g.subject_id =  subjects.id
    JOIN professors p ON p.id = subjects.professor_id
    WHERE students.id = 2
    AND p.id = 4
    """
    result = session.query(Subject.name.label('subject'), Student.name.label('student_name'),
                           Professor.name.label('professor_name')) \
        .join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id) \
        .join(Professor, Subject.professor_id == Professor.id) \
        .filter(and_(Student.id == 2, Professor.id == 4)).distinct().all()
    return result


def select_11():
    """
    SELECT students.name AS student_name,
         p.name AS professor_name,
         ROUND(AVG(g.grade),2) as average_grade
    FROM students
    JOIN grades g ON students.id = g.student_id
    JOIN subjects ON g.subject_id =  subjects.id
    JOIN professors p ON p.id = subjects.professor_id
    WHERE students.id = 2
      AND p.id = 4
    group BY student_name, professor_name
    """
    result = session.query(Student.name.label('student_name'), Professor.name.label('professor_name'),
                           func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Grade, Student.id == Grade.student_id).join(Subject, Grade.subject_id == Subject.id) \
        .join(Professor, Subject.professor_id == Professor.id) \
        .filter(and_(Student.id == 2, Professor.id == 4)).group_by(Student.name, Professor.name).all()
    return result


def select_12():
    """
    SELECT DISTINCT students.name AS students_name,
    grades.grade AS grades_grade,
    grades.date AS grades_date
    FROM students
    JOIN groups ON groups.id = students.group_id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON subjects.id = grades.subject_id
    WHERE groups.name = 'group_1'
      AND subjects.name = 'math'
      AND grades.date =
      (SELECT MAX(date) FROM grades g2
              WHERE g2.student_id = students.id
              AND g2.subject_id = subjects.id
              GROUP BY g2.student_id, g2.subject_id)
    ORDER BY students.name, grades.grade
    """
    """
    SELECT distinct
    groups.name AS group_name, 
    subjects.name AS subject, 
    students.name AS student_name, 
    grades.grade AS grade, 
    anon_1.max_date AS max_date 
    FROM grades 
    JOIN students ON grades.student_id = students.id 
    JOIN groups ON students.group_id = groups.id 
    JOIN subjects ON grades.subject_id = subjects.id 
    JOIN (
        SELECT grades.student_id AS student_id, 
               grades.subject_id AS subject_id, 
               max(grades.date) AS max_date 
        FROM grades 
        GROUP BY grades.student_id, 
                 grades.subject_id
         ) AS anon_1 ON 
              grades.student_id = anon_1.student_id 
              AND grades.subject_id = anon_1.subject_id 
              AND grades.date = anon_1.max_date 
    WHERE groups.id = 1 AND subjects.id = 1 
    ORDER BY students.name
    """

    subquery = session.query(Grade.student_id, Grade.subject_id, func.max(Grade.date).label('max_date')) \
        .group_by(Grade.student_id, Grade.subject_id) \
        .subquery()

    result = session.query(Student.name.label('student_name'), Group.name.label('group_name'),
                           Subject.name.label('subject'), Grade.grade.label('grade'),
                           subquery.c.max_date) \
        .join(Student, Grade.student_id == Student.id) \
        .join(Group, Student.group_id == Group.id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .join(subquery, and_(Grade.student_id == subquery.c.student_id,
                             Grade.subject_id == subquery.c.subject_id,
                             Grade.date == subquery.c.max_date)) \
        .filter(and_(Group.id == 1, Subject.id == 1)) \
        .order_by(Student.name) \
        .distinct().all()
    return result
