from sqlalchemy import create_engine
import os

class learning_db():

    name = os.getenv("NAME")
    password = os.getenv("PASSWORD")
    rds_host = os.getenv("RDS_HOST")
    db_name = os.getenv("DB_NAME")

    def get_connection(engine):
        connection = engine.connect()
        return connection
    def get_engine(self):
        engine = create_engine(f"mysql+pymysql://{self.name}:{self.password}@{self.rds_host}/{self.db_name}",echo = True)
        return engine

