import json


def write(json_object):
    print("<response>"+json.dumps(json_object)+"</response>")