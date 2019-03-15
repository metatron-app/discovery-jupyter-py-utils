import requests


def get(hostname, port, did):

    loginHeaders = {'Authorization': 'Basic cG9sYXJpc19jbGllbnQ6cG9sYXJpcw==', 'Content-Type' : 'application/x-www-form-urlencoded'}
    loginData = {'grant_type':'password', 'scope':'write', 'username':'polaris', 'password':'polaris'}
    loginUrl = "http://" + hostname + ":" + port + "/oauth/token"
    res = requests.post(loginUrl, loginData,  headers=loginHeaders).json()

    # login check
    #print(res)

    token_type = res["token_type"]
    token = res["access_token"]
    auth = token_type + ' ' + token

    #auth value check
    #print('auth:' + auth)

    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': auth}
    url = "http://" + hostname + ":" + port + "/api/datasources/" + did + "/data"

    # url value check
    #print('url:' + url)

    return requests.post(url, headers=headers).json()
