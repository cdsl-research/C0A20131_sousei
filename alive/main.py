import subprocess #subprocessをインポート

import subprocess #subprocessをインポート
def alive(IP,num):#pingを送る関数
    print(IP)
    for ip in IP:
        res = subprocess.run(["ping",str(ip),"-c",str(num), "-W","300"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
        if res.returncode == 0:
            ans = "成功"
        else:
            ans = "失敗"
        print("----------")
    return ans
    
        
#alive(ip, num)[0] #成功　or 失敗
#alive(ip, num)[1] #True or False

def main(**kwargs):
    return alive(kwargs["alive_server_ipaddr"],kwargs["alive_count"])
    