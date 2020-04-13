from datetime import datetime

from test_requests.test_wechat.api.department import Department


class TestDepartment:


    @classmethod
    def setup_class(cls):
        cls.department=Department()


    def test_get_department(self):
        r=self.department.query_department()
        assert r["errcode"]==0

    def test_add_department(self):
        r=self.department.add_department(name="测试自动化",parentid=1)
        assert r["errcode"]==0

    def test_update_department(self):
        r=self.department.query_department()
        department_id=r['department'][0]["id"]
        print(department_id)
        r=self.department.update_department(department_id,name="test11")
        assert r["errcode"]==0

    def test_del_department(self):
        r = self.department.query_department()
        id=r['department'][-1]["id"]
        r=self.department.delete_department(id)
        assert r["errcode"]==0





