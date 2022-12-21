import sqlalchemy
from rds_source.learning_db import learning_db
from datetime import datetime


class RDBMSSource():

    _type_map = {
        3:int,
        4:float,
        5:float,
        6:None,
        12:datetime,
        253:str,
    }

    def __init__(self, query, engine, batch_size = 1000):
        self.query = query
        self.engine = engine
        self.batch_size = batch_size

    def get_data_in_chunks(self):
        '''
        Reads data from an RDS MYSQL table and breaks the read into defined chunks, returns a tuple of: a dict of columns types and a chunk of rows
        '''
        with self.engine.connect() as connection:
            try:
                with connection.connection.cursor() as result_cursor:

                    result_cursor.execute(query)
                    cursor_desc = result_cursor.description

                    full_schema_desc = "\n".join([str(t) for t in cursor_desc])
                    print(f'full schema is as follows: {full_schema_desc}')

                    cursor_dict = {column[0]:self._type_map.get(column[1]) for column in cursor_desc}
                    result_cursor.arraysize = 10000

                    while True:
                        chunk = result_cursor.fetchmany(self.batch_size)
                        if not chunk:
                            break
                        yield cursor_dict, chunk

            except Exception as e:
                print(f"error executing query - exception raised {e}")
                raise
            finally:
                connection.close()

if __name__ == "__main__":
    db_factory = learning_db()
    engine = db_factory.get_engine()
    query = 'select * from learning.grades'
    BATCH_SIZE = 5
    source = RDBMSSource(query, engine, 10)
    for header, chunk in source.get_data_in_chunks():
        for row in chunk:
            print(row)
        print("+ new chunk now +")
