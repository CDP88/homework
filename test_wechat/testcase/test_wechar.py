from test_requests.test_wechat.api.wechar import WeChar


class TestWechar:


    @classmethod
    def setup_class(cls):
        cls.token=WeChar.get_token()

    def test_get_token(self):
        r=WeChar.get_access_token(WeChar.secret)
        assert r["errcode"]==0

    def test_token_exist(self):
        assert self.token is not None
