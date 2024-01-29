import time
import requests


def login(id):
    u = 'cnmcnmcnm'
    p = 'wcnmwcnmwcnm'

    # 发起 HTTP 请求
    url = "http://kujijis.icu/wen/status.php?action=add"
    params = {'u': u, 'p': p, 'id': str(id), 'system_str': 'PC'}
    response = requests.get(url, params=params)

    # 检查响应是否成功
    if response.ok:
        print('1')
        try:
            # 尝试解析JSON
            
            res = response.json()
            print(res)
            
        except ValueError:
            pass
            # print("服务器返回的内容不是有效的JSON格式")
    else:
        print(f"请求失败，状态码: {response.status_code}")
        exit()


# 示例调用
for i in range(1000000,10000000): 
    if i %1000 ==0:   
        time.sleep(2)
    login(i)
