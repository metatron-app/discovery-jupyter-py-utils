import requests


def get(hostname, port, did):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    url = "http://" + hostname + ":" + port + "/api/dashboards/" + did + "/data"
    return requests.post(url, headers=headers).json()