import requests
import subprocess
import yaml
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
        
def main():
    with open('./conf.yaml','r') as file:
       web1 = yaml.safe_load(file)
       web2 = web1["module"]
       web3 = web2["web"]
       web_count = web3["web_count"]
       web_url = web3["web_url"]
       web(web_url,web_count)
       
       
       
