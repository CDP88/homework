import requests

from test_requests.test_wechat.api.wechar import WeChar


class Department(WeChar):
    get_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    add_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    update_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
    delete_department_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def query_department(self,departmentid=None):
        r=requests.get(self.get_department_url,params={
            "access_token":self.get_token(self.secret),
            "id":departmentid
        })
        self.format(r)
        return r.json()


    def add_department(self,name,parentid,**kwargs):
        data={"name":name,"parentid":parentid}
        data.update(kwargs)
        r=requests.post(self.add_department_url,
                        params={"access_token":self.get_token(self.secret)},
                        json=data)
        self.format(r)
        return  r.json()

    def update_department(self,department_id,**kwargs):
        date={"id": department_id}
        date.update(kwargs)
        r=requests.post(self.update_department_url,params={"access_token":self.get_token(self.secret)},
                        json=date)
        self.format(r)
        return r.json()

    def delete_department(self,id):
        r=requests.get(self.delete_department_url,params={
            "access_token":self.get_token(self.secret),"id":id})
        return r.json()

