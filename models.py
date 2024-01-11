from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# sql_create_groups_table =
"""
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL
    );

"""

# sql_create_students_table =
"""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
"""

# sql_create_professors_table =
"""
CREATE TABLE IF NOT EXISTS professors (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL
    );
"""

# sql_create_subjects_table =
"""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    professor_id INTEGER NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professors (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
"""

# sql_grades_table =
"""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    grade INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE    
    );
"""


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    group_id = Column('group_id', ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    group = relationship('Group', backref='students')

class Professor(Base):
    __tablename__ = 'professors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    professor_id = Column('professor_id', ForeignKey('professors.id', ondelete='CASCADE', onupdate='CASCADE'))
    professor = relationship('Professor', backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, nullable=False)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    student = relationship('Student', backref='grades')
    subject_id = Column('subject_id', ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject = relationship('Subject', backref='grades')
    date = Column(Date, nullable=False)