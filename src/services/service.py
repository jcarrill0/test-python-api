import requests
from datetime import datetime

class Service:

    def __init__(self, indicator, date):
        self.indicator = indicator
        self.date = date

    def get_info_by_date(self):
        objDate = datetime.strptime(self.date, '%d-%m-%Y')
        # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
        url = f'https://mindicador.cl/api/{self.indicator}/{self.date}'
        response = requests.get(url)
        jsonInfo = response.json()
        data = jsonInfo.get('serie')[0]

        return data
        