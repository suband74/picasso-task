import click
import logging.config

from settings import logger_config
from connect import create_connection

logging.config.dictConfig(logger_config)

logger = logging.getLogger('main.cr_db')


@click.command()
def create_table():
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS police (id serial PRIMARY KEY, Crime_Id INTEGER, Original_Crime_Type_Name VARCHAR, Report_Date TIMESTAMP, Call_Date TIMESTAMP, Offense_Date TIMESTAMP, Call_Time TIME, Call_Date_Time TIMESTAMP, Disposition VARCHAR, Address VARCHAR, City VARCHAR, State VARCHAR, Agency_Id INTEGER, Address_Type VARCHAR, Common_Location VARCHAR);")
    except:
        logger.exception('table did not create')

    logger.info('Successfully created table')
    conn.commit()
    conn.close()
    cur.close()

if __name__ == '__main__':
  create_table()
