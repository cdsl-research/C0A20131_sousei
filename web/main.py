import requests
import subprocess
def web(url,num):
    num2 = 0
    while True:
        if num2 == num:
            break
        Url_r = subprocess.run(["curl","-LIs",url],stdout = subprocess.PIPE)
        print(Url_r.stdout.decode("cp932"))
        if Url_r.returncode == 0:
            print("成功")
        else:
            return "失敗"
        print("----------")
        num2 += 1
        
def main(**kwargs):
    web(kwargs["web_url"],kwargs["web_count"])
    
    
       
       
