from datetime import datetime
from django.db import connection
from apps.constants import *

import pytz

IST = pytz.timezone('Asia/kolkata')
today = datetime.now().strftime("%Y%m%d")
nowtime = datetime.now().strftime("%H%M%S")
financialyear = 24

def getToday():
    return datetime.now().strftime("%Y%m%d")


def getlocaltime():
    datetime_ist = datetime.now(IST)
    curr_clock = datetime_ist.strftime("%H%M%S")
    return curr_clock


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]

    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
