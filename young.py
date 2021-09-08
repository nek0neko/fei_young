import requests
import datetime
import time
import re

def fun2():
    url = "http://100.64.0.1"
    response = requests.get(url, allow_redirects=False)
    url1 = response.headers['Location']
    #ip = input("ip:")
    #mac = input("mac:")
    #url1 = "http://58.53.199.144:8001?userip=" + ip + "&wlanacname=&nasip=59.172.216.61&usermac=" + mac
    print(url1)
    #print(url1)
    url2 = url1 + "&aidcauthtype=0"
    header = {
        'Host': '58.53.199.144:8001',
        'User-Agent': 'CDMA+WLAN(macos)',
        'ClientVersion': 'Mswx'
    }
    # print(url2)
    response = requests.get(url2, headers=header)
    print(response.headers['Set-Cookie'])
    res = re.search('CDATA\[(.*)\]\]', response.text, re.M | re.I | re.S)
    if res is None:
        exit()
    url = res.groups()[0]
    print(url)
    header = {
        "Host": "58.53.199.144:8001",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "ClientVersion": "Mswx",
        "Cache-Control": "no-cache",
        "Accept-Language": "zh-cn",
        "User-Agent": "CDMA+WLAN(macos)",
        "Content-Type": "application/x-www-form-urlencoded",
        "cookie": response.headers['Set-Cookie']
    }
    payload = {"button": "Login",
               "UserName": "****************",
               "Password": "****************",
               "FNAME": "0",
               "OriginatingServer": "http://www.sina.com.cn/"
               }
    res1 = requests.post(url, headers=header, data=payload)
    print(res1.text)
    res = re.search('认证成功', res1.text, re.M | re.I | re.S)
    if res:
        obj = open("./net.log", "a")
        strs = datetime.datetime.now()
        strs = str(strs)
        obj.write(strs + " Network Restart Succeed\n")
        obj.close()
    else:
        obj = open("./net.log", "a")
        strs = datetime.datetime.now()
        strs = str(strs)
        obj.write(strs + " Network Restart Failed\n")
        obj.close()

def fun1():
    count = 0
    try:
        q = requests.get("https://www.baidu.com", timeout=5)
        m = re.search(r'STATUS OK', q.text)
        if m:
            return True
        else:
            return False
    except:
        print("error")

if __name__ == "__main__":
    count = 0
    for i in range(5):
        obj = open("./net.log", "a")
        net = fun1()
        if not net:
            count += 1
            strs = datetime.datetime.now()
            strs = str(strs)
            str1 = str(count)
            obj.write(strs + " Network Error " + str1 + "\n")
            if count == 5:
                obj.write(strs + " network Restart\n")
                fun2()
        else:
            count = 0
            strs = datetime.datetime.now()
            strs = str(strs)
            obj.write(strs + " Network OK\n")
        obj.close()
        time.sleep(1)


