import requests
import json
import login

result2=login.login()
success2=result2.get('success')
msg2=result2.get('msg')
print(msg2)
#print(result2)

if msg2=='登录成功':
    #def listinfo():
    url = "http://content.test.17zuoye.net/search/api/paper/list"
    headers = {'Content-Type': 'application/json;charset=utf-8','Cookie':'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215239145%22%2C%22first_id%22%3A%2217824a5cb1bbff-09617ee324760c-53e356a-2073600-17824a5cb1c2d7%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217824a5cb1bbff-09617ee324760c-53e356a-2073600-17824a5cb1c2d7%22%7D; voxauth=yBgrQd+hs752ztuNxNJZwOJFw1+l74sV2Ve7YVmoUSoMJucM/KIpZNle85sikZaV5DpK75WD6cuuVYXZerDrGg; va_sess=yBgrQd+hs752ztuNxNJZwOJFw1+l74sV2Ve7YVmoUSoMJucM/KIpZNle85sikZaV5DpK75WD6cuuVYXZerDrGg; uid=13070714; session=.eJxNj8GKwzAMRP9F57JYtmxZue439BzkSKaBUpbUOZRl_70hvewc5jIzMO8X5r758wbT2Ha_wLwaTBA1EyKZqgaSzC0XbMtSSYMZiZSee0wpclUpbtrUTmuJgzsjExlZ79zJQ88snlxTb4WFjlbzYMiLqJWI0haP0krJaEGxFjGHC6zmj7GO15fu4zaP14_D9Njv93_JefX7OodTsVJKdCz3p28fDMz1oEhYa4S_Nyp0RTI.YHlr1Q.y6vcMM4WlMl5ooNKAdo4hQsR2YI'}
    data = {"city": "", "cityArray": {},"district":"","districtArray":{},"grade":0,"is_famous_school_paper":False,"page":0,"paper_type":0,"paper_type_name":"全部","per_page":10,"rating":"","region_code":120000,"region_name":"天津","site":1,"sort_way":"desc","subject_id":101,"title":"","year":0}

    response = requests.post(url, json=data, headers=headers)

    print(response.json())


    #if __name__ == '__main__':
    #    listinfo()
