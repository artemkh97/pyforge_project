import psycopg2
from psycopg2 import Error
import app

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5444",
                                  database="postgres_db")

    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE compound
              (ID INT PRIMARY KEY     NOT NULL,
              COMPOUND        TEXT    NOT NULL,
              NAME            TEXT    NOT NULL,
              FORMULA         TEXT    NOT NULL,
              INCHI           TEXT    NOT NULL,
              INCHI_KEY       TEXT    NOT NULL,
              SMILES          TEXT    NOT NULL,
              CROSS_LINKS_COUNT INT   NOT NULL); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgresSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgresSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgresSQL connection is closed")

    # Executing a SQL query to insert data into  table
    dictionary = app.write_data('ADP')
    columns = dictionary.keys()
    for i in dictionary.values():
        sql2 = '''insert into compound(COMPOUND, NAME, FORMULA, INCHI, INCHI_KEY, SMILES, 
        CROSS_LINKS_COUNT) VALUES{};'''.format(i)

        cursor.execute(sql2)

    sql3 = '''select * from compound;'''
    cursor.execute(sql3)
    for i in cursor.fetchall():
        print(i)

    connection.commit()
    connection.close()

    # Executing a SQL query to delete table
    delete_query = """Delete from compound where id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    # Fetch result
    cursor.execute("SELECT * from compound")
    print("Result ", cursor.fetchall())

