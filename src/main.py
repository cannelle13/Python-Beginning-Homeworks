from dotenv import load_dotenv
import os
from sqlalchemy.orm import (
    declarative_base,
)  # function used to create a base class for declarative SQLAlchemy models
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)  # components used to define the structure of your database tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # cannot have NULL values
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f"This is {self.id} student {self.name}. Age: {self.age}"

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age})>"


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)

    def __str__(self):
        return f"This is {self.id} subject {self.subject_name}"

    def __repr__(self):
        return f"<Subject(id={self.id}, subject_name='{self.subject_name}')>"


class StudentSubject(Base):
    __tablename__ = "student_subject"

    student_subject_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)

    def __repr__(self):
        return f"<StudentSubject(id={self.id}, student_id={self.student_id}, subject_id={self.subject_id})>"


load_dotenv()  # Load from .env file

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# Make a connection to DB
DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(
    DATABASE_URI.format(
        host="localhost",
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        port=5432,
    )
)

#  Join our connection with our class
Base.metadata.create_all(engine)

# Open session to DB import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

# Find all students` name that visited 'English' classes
english_students = (
    session.query(Student.name, Subject.subject_name)
    .join(StudentSubject, Student.id == StudentSubject.student_id)
    .join(Subject, Subject.subject_id == StudentSubject.subject_id)
    .filter(Subject.subject_name == "English")
    .all()
)

print(english_students)

# Present human-readable output
names = [student[0] for student in english_students]
names_str = " and ".join(names)
result_message = f"Students {names_str} visited English classes."
print(result_message)
