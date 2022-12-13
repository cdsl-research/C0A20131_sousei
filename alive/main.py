import subprocess #subprocessをインポート
import yaml
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
def main():
    with open('../conf.yaml','r') as file:
        alive1 = yaml.safe_load(file)
        alive2 = alive1["module"]
        alive3 = alive2["alive"]
        alive_count = alive3["alive_count"]
        alive_server_ipaddr = alive3["alive_server_ipaddr"]
        alive(alive_server_ipaddr,alive_count)
        
       

if __name__ == '__main__':
    main()
    