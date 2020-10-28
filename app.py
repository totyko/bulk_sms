#!/usr/bin/env python3
import json
import requests

api_url = "https://api.bulksms.com/v1"


print('Enter number Int Fmt')
to_number = str(input())
print('Enter msj text')
body_text = str(input())


mensaje = {}

mensaje['to'] = to_number
mensaje['body'] = body_text

json_data = json.dumps(mensaje, indent = 4)
print(json_data)

r = requests.post(api_url, headers={"Authorization": "Basic "}, data=json_data)
print(r.status_code)
