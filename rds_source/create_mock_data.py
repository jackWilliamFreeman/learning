import data_generator as dg
from sqlalchemy.orm import sessionmaker
from learning_db import learning_db
import time


class MockDataGenerator():
    def __init__(self, engine) -> None:
        self.engine = engine

    def insert_mock_data_over_time(self, num_loops = 1000):
        i = 0
        while(i <= num_loops):
            student = dg.generate_students_with_grades(1)
            Session = sessionmaker(bind = self.engine)
            session = Session()
            session.add_all(student)
            session.commit()
            print(f'Added {i+1} student')
            time.sleep(2)
            i += 1
        session.close()

    def insert_mock_data_batch(self, num_students):
        students = dg.generate_students_with_grades(num_students)
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add_all(students)
        session.commit()
        session.close()

db_factory = learning_db()
engine = db_factory.get_engine()
mdg = MockDataGenerator(engine)
mdg.insert_mock_data_batch(200)