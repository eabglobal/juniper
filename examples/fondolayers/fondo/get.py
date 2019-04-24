import requests
from minik.core import Minik

app = Minik()


@app.route('/events', methods=['GET'])
def get_handler():
    r = requests.get('https://api.github.com/events')
    return {'data': r.json()}
