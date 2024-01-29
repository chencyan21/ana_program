import requests

def login():
    u = '12345678'
    p = 'wcnmwcnmwcnm'

    # 发起 HTTP 请求
    url = "http://kujijis.icu/wen/status.php?action=add"
    params = {'u': u, 'p': p, 'id': 'system_str', 'system_str': 'PC'}  # 请替换 system_str
    response = requests.get(url, params=params)
    
    # 解析服务器响应
    res = response.json()
    if res['code'] == 1:
        print(f"登录成功")
        # 这里可以进行页面跳转或其他操作
    else:
        print("登录失败")

def error(message):
    print(f"错误: {message}")

def has_same_char(s):
    # 判断字符串是否包含相同字符的逻辑，这里简化为只判断是否有重复字符
    return len(set(s)) != len(s)

# 示例调用
login()
