import yaml
def get_ping():#get_ping関数
    with open('./conf.yaml','r',) as file:#yamlファイルを読み込み
        K = yaml.safe_load(file)
        IP = K["IP"]#IPアドレスの追加
        Num = K["Num"]#死活監視回数の追加
        Time = K["Time"]#タイムアウト時間
    return IP,Num,Time

