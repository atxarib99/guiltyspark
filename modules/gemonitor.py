from monitor import Monitor

import subprocess
import json
import requests

class MonitorImpl(Monitor):

    name = 'OSRS-GE-Bond-Monitor'

    def get(self):
        url = 'https://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=13190'
        response = requests.get(url)
        return response.json()
