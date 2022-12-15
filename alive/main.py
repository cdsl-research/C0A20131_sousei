import subprocess #subprocessをインポート

def alive(IP,num):#pingを送る関数
    print(IP)
    for ip in IP:
        res = subprocess.run(["ping",str(ip),"-c",str(num), "-W","300"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
        if res.returncode == 0:
            print("成功")
            
        else:
            print("失敗")
            return False
        print("----------")
def main(**kwargs):
    alive(kwargs["alive_server_ipaddr"],kwargs["alive_count"])
    