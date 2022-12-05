from DNS import DNS_rule
from Alive import ping_rule
from path import path_rule
import yaml
def print_DNS():
    with open("conf.yaml","r") as file:
        DNS_k = yaml.safe_load(file)
        DNS_k2 = DNS_k["method"] 
        DNS_k3 = DNS_k2["DNS"]
        DNS_k4 = DNS_k3["Domeine"]
        DNS_IP = DNS_k3["IP"]
        print(DNS_IP)
        DNS_S = DNS_rule.DNS_rule2(DNS_k4)
        if DNS_S == "失敗":
            Alive_S = ping_rule.Post_Ping(DNS_IP)
            if Alive_S == "失敗":
                Path_S = path_rule.Path(DNS_IP)
                if Path_S == "失敗":
                    print("経路に問題あり")
                
                
            if Alive_S == "成功":
                print("DNSサーバー内に問題あり.")
       
        
