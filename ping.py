import yaml #yamlファイルのインポート
import schedule #scheduleをインポート
import datetime #datetimeをインポート
import time #timeをインポート
import subprocess #subprocessをインポート

def get_ping():#get_ping関数
        IP = [] #IPアドレス
        Count = [] #死活監視の回数
        Time = [] #タイムアウトの時間
        with open('../rennsyuu.yaml','r',) as file:#yamlファイルを読み込み
            IP_dict = yaml.safe_load(file)
        for i in IP_dict.keys():
            IP.append(IP_dict[i]["IP"])#IPアドレスの追加
            Count.append(IP_dict[i]["Count"])#死活監視回数の追加
            Time.append(IP_dict[i]["Time"])#タイムアウト時間
        print("IPアドレス")
        print(IP)
        print("死活監視の回数")
        print(Count)
        print("タイムアウト時間")
        print(Time)
        return IP,Count,Time

def Post_Ping(IP,Count,Time):#pingを送る関数
    val = 0
    for ip in IP:
        res = subprocess.run(["ping",ip,"-c",str(Count[val]), "-W", str(Time[val])],stdout=subprocess.PIPE)##-cは疎通確認の回数、-Wは死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
        if res.returncode == 0:
            print("成功")
        else:
            print("失敗")
        print("----------")
        val += 1
