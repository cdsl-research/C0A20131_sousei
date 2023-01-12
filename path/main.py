import subprocess
def path(IP,num):#pingを送る関数
    print(IP)
    for ip in IP:
        res = subprocess.run(["ping","-R",str(ip),"-c",str(num)],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
        if res.returncode == 0:
            ans = "成功"
        else:
            ans = "失敗"
        print("----------")
    return ans
    
def main(**kwargs):
    return path(kwargs["path_server_ipaddr"],kwargs["path_count"])
        
