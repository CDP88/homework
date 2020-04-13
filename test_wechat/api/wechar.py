import json

import requests


class WeChar:
    token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid='ww6de619f6815b093e'
    secret="PUt4lZK9P-YATRdYDTTPerBxvuCype-PdLDa-0s5p0Y"
    # secret="aIiolNCSPNP1CBzGbFjSSD8mWkuduBJg3bdBiVhFBSQ"
    token={}

    @classmethod
    def get_token(cls,secret=secret):
        r=cls.get_access_token(secret)
        if secret not in cls.token:
            cls.token[secret]=r["access_token"]
            return cls.token[secret]
        else:
            return cls.token[secret]


    @classmethod
    def get_access_token(cls,secret):
        r = requests.get(cls.token_url, params={
            "corpid": cls.corpid,
            "corpsecret": secret
        })
        cls.format(r)
        assert r.json()["errcode"]==0
        return  r.json()

    @classmethod
    def format(cls,r):
        print(json.dumps(r.json(),indent=2))

