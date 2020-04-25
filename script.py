
import requests


r = requests.get('https://siltonstailoring.com')
print(r.status_code)
print(r.ok)
