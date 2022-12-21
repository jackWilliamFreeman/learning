from sqlalchemy import create_engine
import os

class learning_db():

    def __init__(self) -> None:
        self.name = os.getenv("NAME")
        self.password = os.getenv("PASSWORD")
        self.rds_host = os.getenv("RDS_HOST")
        self.db_name = os.getenv("DB_NAME")

    def get_connection(engine):
        connection = engine.connect()
        return connection

    def get_engine(self):
        engine = create_engine(f"mysql+pymysql://{self.name}:{self.password}@{self.rds_host}/{self.db_name}",echo = True)
        return engine

