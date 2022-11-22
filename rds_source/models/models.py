from sqlalchemy import  Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    '''class for students table in sql alchemy'''
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    created_on = Column(DATETIME)
    created_by = Column(String(100))
    modified_on = Column(DATETIME)
    modified_by= Column(String(100))
    grades = relationship('Grade', backref = 'student')

class Grade(Base):
    '''class for grades table in sql alchemy'''
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(100))
    score = Column(Integer)    
    created_on = Column(DATETIME)
    created_by = Column(String(100))
    modified_on = Column(DATETIME)
    modified_by= Column(String(100))
    student_id = Column(Integer, ForeignKey("students.id"))

def get_base():
    return Base