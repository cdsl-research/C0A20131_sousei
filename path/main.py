import subprocess
import yaml
def Path(IP,num):#pingを送る関数
    print(IP)
    for ip in IP:
        res = subprocess.run(["ping","-R",str(ip),"-c",str(num)],stdout=subprocess.PIPE)##-cは疎通確認の回数、-W>は死活監視のタイムア>ウト指定(300m秒)
        print(res.stdout.decode("cp932"))
    
        if res.returncode == 0:
            print("成功")
        else:
            return False
        print("----------")
    
def main():
    with open('../conf.yaml','r') as file:
        path1 = yaml.safe_load(file)
        path2 = path1["module"]
        path3 = path2["path"]
        path_count = path3["path_count"]
        path_server_ipaddr = path3["path_server_ipaddr"]
        Path(path_server_ipaddr,path_count)
        
if __name__ == '__main__':
    main()
    
