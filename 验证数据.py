import requests
import json
import login

result2=login.login()
success2=result2.get('success')
msg2=result2.get('msg')
print(msg2)
print(result2)

if msg2=='登录成功':
    #def listinfo():
    url = "http://content.test.17zuoye.net/search/api/paper/list"
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {"city": "", "cityArray": {},"district":"","districtArray":{},"grade":0,"is_famous_school_paper":False,"page":0,"paper_type":0,"paper_type_name":"全部","per_page":10,"rating":"","region_code":120000,"region_name":"天津","site":1,"sort_way":"desc","subject_id":101,"title":"","year":0}

    response = requests.post(url, json=data, headers=headers)

    print(response.json())


    #if __name__ == '__main__':
    #    listinfo()
