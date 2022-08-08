from datetime import datetime
import csv
import click
import logging.config

from settings import logger_config
from connect import create_connection

logging.config.dictConfig(logger_config)

logger = logging.getLogger('main.ins_db')

def time_of_function(function):
    def wrapped(*args):
        start_time = datetime.now()
        res = function(*args)
        print(datetime.now() - start_time)
        return res
    return wrapped 

@click.command()
@time_of_function
def insert_database():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM police")
    c = cur.fetchall()[0][0]
    if c == 0:
        with open('police-department-calls-for-service.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            reader = list(reader)[1::]
            num = 0
            for row in reader:
                row[2] = row[2].replace('T', ' ')
                row[3] = row[3].replace('T', ' ')
                row[4] = row[4].replace('T', ' ')
                row[6] = row[6].replace('T', ' ')
                if len(row) == 13:
                    row.append(None)
                try:
                    cur.execute("INSERT INTO police (Crime_Id, Original_Crime_Type_Name, Report_Date, Call_Date, Offense_Date, Call_Time, Call_Date_Time, Disposition, Address, City, State, Agency_Id, Address_Type, Common_Location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s);", row)
                    num += 1
                    print(num)
                except:
                    logger.exception("Unable to insert")

    conn.commit()
    logger.info('successfully insert')
    conn.close()
    cur.close()

if __name__ == '__main__':
    insert_database()