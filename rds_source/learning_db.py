from sqlalchemy import create_engine

class learning_db():
    rds_host  = "database-1.ci9xxovcnbmy.ap-southeast-2.rds.amazonaws.com"
    name = 'jack'
    password = 'roose1velt'
    db_name = "learning"

    def get_connection(engine):
        connection = engine.connect()
        return connection
    def get_engine(self):
        engine = create_engine(f"mysql+pymysql://{self.name}:{self.password}@{self.rds_host}/{self.db_name}",echo = True)
        return engine

