from log import log_rule
from Alive import ping_rule
from path import path_rule
import yaml
def log_print():
    with open('conf.yaml') as file:
        log = yaml.safe_load(file)
        log1 = log["method"]
        log2 = log1["log"]
        log3 = log2["path"]
        log_IP = log2["IP"]
        print(log3)
        print(log_IP)

        log_c = log_rule.log_rule2(log3)
        print(log_c)
        if log_c == 0:
            Alive_S = ping_rule.Post_Ping(log_IP)
            if Alive_S == "失敗":
                Path_S = path_rule.Path(log_IP)
                if Path_S == "失敗":
                    print("経路に問題あり")
                
                
            if Alive_S == "成功":
                print("DNSサーバー内に問題あり.")
       
log_print()
