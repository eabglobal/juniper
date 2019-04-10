import requests
from minik.core import Minik

app = Minik()


@app.route('/events', methods=['GET'])
def get_handler():
    return {'data': ['hello', 'world']}
