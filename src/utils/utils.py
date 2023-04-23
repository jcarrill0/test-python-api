from flask import jsonify
from datetime import datetime

def validate_min_date(date):
    minDate = datetime.strptime('01-01-2013', '%d-%m-%Y')
    currentDate = datetime.strptime(date, '%d-%m-%Y')

    return True if currentDate < minDate else False