import requests
import subprocess
def web_r(url):
    rq = requests.get(url,allow_redirects = False)
    

    return rq.status_code,rq.reason

def Web_r(url):
    Url_r = subprocess.run(["curl","-LIs",url],stdout = subprocess.PIPE)
    print(Url_r.stdout.decode("cp932"))
    if Url_r.returncode == 0:
        return "成功"
    else:
        return "失敗"
    print("----------")
