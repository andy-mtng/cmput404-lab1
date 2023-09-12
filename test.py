import requests

url = "https://raw.githubusercontent.com/andy-mtng/cmput404-lab1/main/test.py"
res = requests.get(url)

print(res.text)
