import subprocess
def Path(IP):#pingを送る関数
    print(IP)
    # for ip in IP:
    res = subprocess.run(["ping","-R",str(IP),"-c","4"],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
    print(res.stdout.decode("cp932"))
    
    if res.returncode == 0:
        return "成功"
    else:
        return "失敗"
    print("----------")
    
    
