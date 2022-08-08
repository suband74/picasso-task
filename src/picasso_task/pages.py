import click
import logging.config

from settings import logger_config
from connect import create_connection

logging.config.dictConfig(logger_config)

logger = logging.getLogger('main.pages')

@click.command()
@click.option('--num', default=0, help='First ID in page.')
@click.option('--date_from', prompt='date from')
@click.option('--date_to', prompt='date to')
def select_pages(date_from, date_to, num):
    conn = create_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM police WHERE Report_Date BETWEEN %s and %s and id > %s LIMIT 20", [date_from, date_to, num])
        for row in cur:
            print(row)
        
    except:
        logger.exception("Unable to select")
    logger.info('Successfully selected')
    conn.close()
    cur.close()

if __name__ == '__main__':
    select_pages()