import subprocess #subprocessをインポート
def Post_Ping(IP):#pingを送る関数
    print(IP)
    for ip in IP:
        res = subprocess.run(["ping",str(ip),"-c","4", "-W","300"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
        if res.returncode == 0:
            print("成功")
            
        else:
            print("失敗")
            return "失敗"
        print("----------")
    
    



    

