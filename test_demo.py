import requests


def test_demo():
    r=requests.get("https://httpbin.testing-studio.com/get",
                   params={
                       "a":1
                   }
                   )
    print(r.json())
    assert r.status_code==200

def test_demo():
    r=requests.get("https://httpbin.testing-studio.com/get",
                   params={
                       "a":1
                   }
                   )
    # print(r.json())
    print(r.text)
    assert r.status_code==200