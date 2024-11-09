import requests


def request_baidu():
    r = requests.get("https://www.baidu.com")
    print(r.status_code)
    print(r.text)
    return
