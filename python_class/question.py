import datetime
import yaml
import select_m
import time
dt = datetime.datetime.today()
iplist = []
iplist2 = []
iplist3 = []
step = input("何秒おきに監視しますか?")

while True:
    question1 = input("何の監視をしますか?")
    if len(question1) == 0:
        break
    question2 = int(input("何台？"))
    
    if question1 == "DNS":
        question3 = input("ドメインを入力してください")
        if question3 =="":
            question3 = "none"
        for i in range(question2):
            ip = input((f'{i}番目のサーバーのIPアドレスを入力'))
            iplist.append(ip)
            if iplist == "":
                iplist.append("none")
        qestion4 = input("ほかのサーバーがありますか？")
        if qestion4 == "yes":
            continue
        else:
            break
        
    if question1 == "Web":
        qestion5 = input("urlを入力してください:")
        
        if qestion5 == "":
            qestion5 = "none"
        for i in range(question2):
            ip = input((f'{i}番目のサーバーのIPアドレスを入力'))
            iplist2.append(ip)
            if iplist2 == "":
                iplist2.append("none")
        qestion4 = input("ほかのサーバーがありますか？")
        if qestion4 == "yes":
            continue
        else:
            break

    if question1 == "log":
        qestion6 = input("ファイルパスを入力して下さい")
            
        if qestion6 == "":
            qestion6 = "none"
        for i in range(question2):
            ip3 = input((f'{i}番目のサーバーのIPアドレスを入力'))
            iplist3.append(ip3)
            if iplist3 == "":
                iplist3.append("none")
        qestion4 = input("ほかのサーバーがありますか？")
        if qestion4 == "yes":
            continue
        else:
            break

        
with open(f"conf.yaml","w") as f:
        yaml.dump({
            "method": {
                "DNS": {
                    "Domeine": question3,
                    "IP": iplist
                },
                "Web": {
                    "URL": qestion5,
                    "IP": iplist2
                },
                "log": {
                    "path": qestion6,
                    "IP": iplist3
                },
                "Step": step
                
            }
                },f,default_flow_style=False)
        
with open(f"{dt}.yaml","w") as f:
        yaml.dump({
            "method": {
                "DNS": {
                    "Domeine": question3,
                    "IP": iplist
                },
                "Web": {
                    "URL": qestion5,
                    "IP": iplist2
                },
                "log": {
                    "path": qestion6,
                    "IP": iplist3
                },
                "Step": step
                   
                
            }
                },f,default_flow_style=False)
        

with open('conf.yaml','r') as file:
         sel = yaml.safe_load(file)
         sel2 = sel["method"]
         sel3 = sel2["Step"]
         cnt = 0      
         while True:
            selct = select_m.get_select()
            print(selct)
            time.sleep(int(sel3))
            cnt +=1
            
            

    
        

    
        
    
        

 



    
    
