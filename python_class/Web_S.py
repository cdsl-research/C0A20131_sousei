from web import web_rule
from Alive import ping_rule
from path import path_rule
import yaml
def print_Web():
    with open("conf.yaml","r") as file:
        Web_k = yaml.safe_load(file)
        Web_k2 = Web_k["method"]
        Web_k3 = Web_k2["Web"]
        Web_k4 = Web_k3["URL"]
        Web_IP = Web_k3["IP"]
        Web_S = web_rule.Web_r(Web_k4)
        print(Web_S)
        if Web_S == "失敗":
            print("死活監視を実行")
            Alive_S = ping_rule.Post_Ping(Web_IP)
            if Alive_S == "失敗":
                Path_S = path_rule.Path(Web_IP)
                if Path_S == "失敗":
                    print("経路に問題あり")
                else:
                    print("サーバーが落ちています")
            else:
                print("Webサーバー内に問題あり.")

            

