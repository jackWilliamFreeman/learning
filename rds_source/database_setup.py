import sys
sys.path.append('../rds_source')
from learning_db import learning_db
from sqlalchemy.orm import sessionmaker
from models.models import get_base
from data_generator import generate_students_with_grades

def create_db_tables():
    db = learning_db()
    engine = db.get_engine()
    base = get_base()
    base.metadata.create_all(engine)

def seed_students():  
    db = learning_db()
    engine = db.get_engine()
    Session = sessionmaker(bind = engine)
    session = Session()
    students = generate_students_with_grades(100)
    session.add_all(students)
    session.commit()

create_db_tables()
seed_students()


