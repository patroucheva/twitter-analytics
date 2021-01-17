import logging
import os

from datetime import datetime

date = datetime.today()
log_file = f'{date.strftime("%Y%m%d")}.log'
log_dir = f'{date.year}/{date.month}/{date.day}'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(filename=log_file, encoding='utf-8', level=logging.DEBUG)

